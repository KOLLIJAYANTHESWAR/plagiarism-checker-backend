# 🔍 Advanced Plagiarism Detection Suite – Backend

An AI-powered plagiarism detection backend built using **Flask, Sentence Transformers, Scikit-learn, and OpenRouter API**.

This backend provides semantic similarity scoring, GitHub code comparison, article-level plagiarism detection, report generation, and AI-based paraphrasing.

---

## 📌 Project Overview

The backend engine powers a multi-modal plagiarism detection platform capable of:

- Semantic similarity analysis using transformer embeddings
- Lexical and structural similarity scoring
- GitHub repository-based code plagiarism detection
- Web-scale article matching using Tavily API
- AI-powered text & code paraphrasing
- Detailed plagiarism report generation

This system is designed for integration with a modern frontend (Next.js / React) or any external client via REST APIs.

---

## 🏗️ Backend Architecture

```
Client (Frontend / API Consumer)
        ↓
Flask REST API
        ↓
Similarity Engine
        ↓
SentenceTransformer Model (all-MiniLM-L6-v2)
        ↓
Cosine Similarity + Lexical + Structural Analysis
        ↓
External APIs:
   - GitHub API
   - Tavily API
   - OpenRouter API
        ↓
Structured JSON Response
```

---

## 🚀 Core Features

### 🔍 Multi-Layer Similarity Scoring

The backend computes:

- **Semantic Similarity** (Transformer embeddings + cosine similarity)
- **Lexical Similarity** (Word overlap ratio)
- **Structural Similarity** (Code structure analysis)
- **Final Weighted Plagiarism Score**

Scoring Logic:

```
Code:
0.4 * Semantic + 0.3 * Lexical + 0.3 * Structural

Text:
0.6 * Semantic + 0.4 * Lexical
```

---

### 💻 GitHub Code Plagiarism Detection

- Extracts function names from input code
- Queries GitHub Code Search API
- Fetches raw file content
- Extracts relevant function block
- Computes similarity score
- Returns best matching repository with confidence score

---

### 📄 Article Plagiarism Detection

- Uses Tavily Search API
- Searches for related web content
- Compares semantic similarity
- Returns matched snippets with similarity score

---

### 🔄 AI De-Plagiarization Engine

Supports two modes:

**Text Mode**
- Uses Parrot (T5-based paraphraser)

**Code Mode**
- Uses OpenRouter API (Mistral-7B-Instruct)
- Extracts rewritten code block
- Preserves functionality while modifying structure

---

### 📊 Detailed Report Generation

Endpoint returns:

- Semantic similarity
- Lexical similarity
- Structural similarity
- Final score
- Status (Original / Plagiarised)
- Highlighted matching words (HTML mark tags)

---

## 🛠️ Tech Stack

### Backend Framework
- Flask
- Flask-CORS

### AI & NLP
- SentenceTransformers (all-MiniLM-L6-v2)
- Scikit-learn (Cosine Similarity)
- Parrot Paraphraser (T5 Model)

### External APIs
- GitHub REST API
- Tavily API
- OpenRouter API

### Utilities
- NumPy
- Regex processing
- Requests library

---

## 📦 Project Structure

```
backend/
│
├── app.py              # Main Flask application
├── generate.py         # Auxiliary generation utilities
├── requirements.txt    # Python dependencies
├── LICENSE
└── README.md
```

---

## 📡 API Endpoints

### `GET /`
Health check endpoint.

---

### `POST /check_plagiarism`

Request:
```json
{
  "input_code": "...",
  "fetched_code": "...",
  "is_code": true
}
```

Response:
```json
{
  "semantic_similarity": 78.4,
  "lexical_similarity": 65.2,
  "structural_similarity": 80.1,
  "final_plagiarism_score": 74.9,
  "status": "Plagiarised"
}
```

---

### `POST /search_github_code`

Searches GitHub repositories for similar code.

Required:
- `input_code`
- `github_token`

---

### `POST /generate_report`

Generates a detailed plagiarism comparison report.

---

### `POST /deplagiarize`

Modes:
- `text`
- `code`

Requires:
- `openrouter_api_key` (for code mode)

---

### `POST /check_article`

Requires:
- `article_text`
- `tavily_api_key`

Returns matched web sources with similarity scores.

---

## ⚙️ Running Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/plagiarism-backend.git
cd plagiarism-backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## 🔐 Security Notes

- No API keys stored server-side
- API keys passed per request
- Input validation for all endpoints
- Error handling with traceback logging
- CORS enabled for frontend integration

---

## 🎯 Engineering Highlights

✔ Transformer-based semantic similarity  
✔ Multi-layer plagiarism scoring system  
✔ GitHub code intelligence integration  
✔ Web article matching engine  
✔ AI-based paraphrasing system  
✔ Structured REST API architecture  
✔ Clean separation of scoring logic  

---

## 📈 Future Improvements

- Rate limiting & API protection
- JWT-based authentication
- Docker containerization
- GPU acceleration for embeddings
- Persistent result storage
- Model fine-tuning for code similarity

---

## 📄 License

MIT License — Free for learning and portfolio use.

---

## 👨‍💻 Author

**Kolli Jayanth Eswar**

AI Systems & Backend Developer  
Flask | NLP | Transformer Models | API Engineering
