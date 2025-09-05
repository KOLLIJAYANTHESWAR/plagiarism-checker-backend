from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import requests
from parrot.parrot import Parrot
import warnings
import traceback
from tavily import TavilyClient


warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

# Load AI models
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)
model = SentenceTransformer('all-MiniLM-L6-v2')


# -------------------- Similarity Functions --------------------

def get_semantic_similarity(t1, t2):
    emb = model.encode([t1, t2])
    return float(cosine_similarity([emb[0]], [emb[1]])[0][0]) * 100


def get_word_overlap(t1, t2):
    w1, w2 = set(t1.lower().split()), set(t2.lower().split())
    return (len(w1 & w2) / len(w1 | w2)) * 100 if w1 or w2 else 0


def get_structural_similarity(code1, code2):
    def clean_code(code):
        return re.sub(r'[^a-zA-Z_]', '', code)

    c1, c2 = clean_code(code1), clean_code(code2)
    return (len(set(c1) & set(c2)) / len(set(c1) | set(c2))) * 100 if c1 or c2 else 0


def determine_status(score, threshold=50):
    return "Plagiarised" if score >= threshold else "Original"


# -------------------- Routes --------------------

@app.route('/', methods=['GET'])
def home():
    return "✅ Backend Running!"


@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    data = request.get_json()
    input_code = data.get('input_code', '').strip()
    fetched_code = data.get('fetched_code', '').strip()
    is_code = data.get('is_code', True)

    if not input_code or not fetched_code:
        return jsonify({'error': 'Both input_code and fetched_code are required'}), 400

    # Clean fetched code: remove any Markdown or extra text
    import re
    code_match = re.search(r"```(?:python)?\n(.*?)```", fetched_code, re.DOTALL)
    if code_match:
        fetched_code_clean = code_match.group(1).strip()
    else:
        fetched_code_clean = fetched_code

    semantic = get_semantic_similarity(input_code, fetched_code_clean)
    lexical = get_word_overlap(input_code, fetched_code_clean)
    structural = get_structural_similarity(input_code, fetched_code_clean) if is_code else 0

    final = 0.4 * semantic + 0.3 * lexical + 0.3 * structural if is_code else 0.6 * semantic + 0.4 * lexical

    return jsonify({
        'semantic_similarity': round(semantic, 2),
        'lexical_similarity': round(lexical, 2),
        'structural_similarity': round(structural, 2),
        'final_plagiarism_score': round(final, 2),
        'status': determine_status(final),
        'matched_code': fetched_code_clean
    })


@app.route('/search_github_code', methods=['POST'])
def search_github_code():
    data = request.get_json()
    input_code = data.get('input_code', '').strip()
    github_token = data.get("github_token", "").strip()

    if not input_code:
        return jsonify({'error': 'input_code is required'}), 400
    if not github_token:
        return jsonify({'error': 'GitHub token is required'}), 400

    match = re.search(r'def\s+(\w+)', input_code)
    function_name = match.group(1) if match else 'function'

    query = f'"def {function_name}" language:python'
    url = f"https://api.github.com/search/code?q={query}&per_page=5"

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'GitHub API failed', 'details': response.text}), 500

    results = response.json().get('items', [])
    if not results:
        return jsonify({'fetched_code': '', 'source': 'GitHub', 'confidence': 0.0}), 200

    best_score = 0
    best_match = ''
    best_url = ''

    for item in results:
        try:
            html_url = item['html_url']
            raw_url = html_url.replace('github.com', 'raw.githubusercontent.com').replace('/blob', '')
            code_response = requests.get(raw_url)
            if code_response.status_code != 200:
                continue

            full_code = code_response.text.strip()
            # Extract only the function block
            func_match = re.search(
                rf'def {function_name}\(.*?\):\n(?:\s+.*\n)*',
                full_code
            )
            if not func_match:
                continue
            fetched_code = func_match.group(0)

            if not fetched_code or len(fetched_code) < 20:
                continue

            semantic = get_semantic_similarity(input_code, fetched_code)
            lexical = get_word_overlap(input_code, fetched_code)
            structural = get_structural_similarity(input_code, fetched_code)
            final_score = 0.4 * semantic + 0.3 * lexical + 0.3 * structural

            if final_score > best_score:
                best_score = final_score
                best_match = fetched_code
                best_url = html_url

        except Exception as e:
            print("[ERROR] Matching failed:", e)
            continue

    return jsonify({
        'fetched_code': best_match,
        'source': best_url if best_url else "No source available",
        'confidence': round(best_score, 2)
    })

@app.route('/generate_report', methods=['POST'])
def generate_report():
    try:
        data = request.get_json()
        t1 = data.get("text1", "").strip()
        t2 = data.get("text2", "").strip()
        is_code = data.get("is_code", False)

        if not t1 or not t2:
            return jsonify({"error": "Both text1 and text2 are required"}), 400

        semantic = get_semantic_similarity(t1, t2)
        lexical = get_word_overlap(t1, t2)
        structural = get_structural_similarity(t1, t2) if is_code else 0
        final_score = 0.4 * semantic + 0.3 * lexical + 0.3 * structural if is_code else 0.6 * semantic + 0.4 * lexical

        def highlight(text_base, text_compare):
            words_base = text_base.lower().split()
            words_compare = text_compare.lower().split()
            common = set(words_base) & set(words_compare)
            highlighted = text_base
            for word in common:
                if len(word) > 3:
                    highlighted = re.sub(
                        r'\b(' + re.escape(word) + r')\b',
                        r'<mark>\1</mark>',
                        highlighted,
                        flags=re.IGNORECASE
                    )
            return highlighted

        return jsonify({
            "text1": t1,
            "text2": t2,
            "semantic_similarity": round(semantic, 2),
            "lexical_similarity": round(lexical, 2),
            "structural_similarity": round(structural, 2),
            "final_score": round(final_score, 2),
            "status": determine_status(final_score),
            "highlighted_text1": highlight(t1, t2),
            "highlighted_text2": highlight(t2, t1)
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Failed to generate report: {str(e)}"}), 500


@app.route('/deplagiarize', methods=['POST'])
def deplagiarize():
    try:
        data = request.get_json()
        input_text = data.get("input_text", "").strip()
        mode = data.get("mode", "text")
        openrouter_api_key = data.get("openrouter_api_key", "").strip()

        if not input_text:
            return jsonify({"error": "input_text is required"}), 400

        rewritten = input_text

        if mode == "text":
            results = parrot.augment(input_phrase=input_text, do_diverse=True, max_return_phrases=10)
            if results:
                for phrase, score in results:
                    if phrase.lower() != input_text.lower():
                        rewritten = phrase
                        break

        elif mode == "code":
            if not openrouter_api_key:
                return jsonify({"error": "OpenRouter API key is required"}), 400

            prompt = f"Rewrite this code to avoid plagiarism but keep functionality:\n\n{input_text}"

            headers = {
                "Authorization": f"Bearer {openrouter_api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "mistralai/mistral-7b-instruct",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }

            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

            if response.status_code != 200:
                return jsonify({"error": f"OpenRouter API failed", "trace": response.text}), 500

            rewritten_raw = response.json()["choices"][0]["message"]["content"].strip()

            # Extract only the code inside ```python``` or ``` blocks
            import re
            code_match = re.search(r"```(?:python)?\n(.*?)```", rewritten_raw, re.DOTALL)
            if code_match:
                rewritten = code_match.group(1).strip()
            else:
                # fallback: return full text if no code block
                rewritten = rewritten_raw

        else:
            return jsonify({"error": "Invalid mode"}), 400

        return jsonify({"deplagiarized_text": rewritten})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Failed to de-plagiarize: {str(e)}"}), 500
    
@app.route('/check_article', methods=['POST'])
def check_article():
    try:
        data = request.get_json()
        article_text = data.get("article_text", "").strip()
        tavily_api_key = data.get("tavily_api_key", "").strip()

        if not article_text:
            return jsonify({"error": "article_text is required"}), 400
        if not tavily_api_key:
            return jsonify({"error": "Tavily API key is required"}), 400

        # Initialize Tavily client
        client = TavilyClient(api_key=tavily_api_key)

        # Search for similar articles
        results = client.search(query=article_text, num_results=5).get("results", [])

        formatted_results = []
        for item in results:
            snippet = item.get("content", "").strip()  # matched content/snippet
            similarity = get_semantic_similarity(article_text, snippet) if snippet else 0

            formatted_results.append({
                "title": item.get("title", "No title"),
                "url": item.get("url", "No URL"),
                "similarity": round(similarity, 2),
                "matched_content": snippet
            })

        return jsonify({
            "input_text": article_text,
            "matches": formatted_results
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Failed to check article: {str(e)}"}), 500

# -------------------- Run Flask App --------------------

if __name__ == '__main__':
    app.run(debug=True)
