🔍 Advanced Plagiarism Detection Backend
<div align="center">

🚀 Backend APIs for AI-powered plagiarism detection and paraphrasing with text, code, and article support.
🌟 Features
 • 🛠️ Installation
 • ⚙️ Configuration
 • 📖 Usage
 • 🐍 Project Structure

</div>
🌟 Features:
🔍 Plagiarism & Similarity Detection
📝 Text Plagiarism Checker - Semantic, lexical, and structural analysis of input text
💻 Code Plagiarism Scanner - GitHub code search and similarity scoring
📄 Article Plagiarism Analyzer - Web content matching using Tavily API
🔄 AI Paraphrasing Tool - De-plagiarize text or code while preserving meaning and functionality

🚀 Technology Stack:
⚡ Flask - Lightweight Python web framework for API endpoints
🤖 AI Models - Sentence Transformers for semantic similarity, Parrot for text paraphrasing
📊 Scikit-learn - Cosine similarity calculations for text/code
🔒 Secure API Integration - GitHub, OpenRouter, and Tavily API keys required
🧪 Async-safe Web Search - For article content matching with throttling and error handling


🛠️ Installation
Prerequisites
Python 3.11+
pip or poetry for dependencies
Git for version control

Quick Start
# Clone the repository
git clone https://github.com/your-username/plagiarism-checker-backend.git
cd plagiarism-checker-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py

🌐 Access the API
By default, the backend runs at http://localhost:5000

⚙️ Configuration
🔑 API Keys
Backend requires API keys for full functionality. You can provide them in a .env file or through frontend requests.

Service	Purpose	Get API Key	Environment Variable
🤖 OpenRouter	AI paraphrasing	Get API Key
	OPENROUTER_API_KEY
🐙 GitHub	Code similarity search	Get Token
	GITHUB_TOKEN
🔍 Tavily	Article plagiarism search	Get API Key
	TAVILY_API_KEY

⚠️ Make sure your GitHub token has public_repo access for code searches.

🔧 Optional .env Example
# API Keys
OPENROUTER_API_KEY=your_openrouter_key_here
GITHUB_TOKEN=your_github_token_here
TAVILY_API_KEY=your_tavily_key_here

# Server settings
FLASK_ENV=development
PORT=5000

📖 Usage
🔍 Text/Code Plagiarism Check
Endpoint: POST /check_plagiarism

Request JSON:
{
  "input_code": "print('Hello World')",
  "fetched_code": "print('Hello World!')",
  "is_code": true
}

Response JSON: Semantic, lexical, structural similarity, final plagiarism score, status, matched code

💻 GitHub Code Search
Endpoint: POST /search_github_code

Request JSON:
{
  "input_code": "def add(a, b): return a + b",
  "github_token": "<YOUR_GITHUB_TOKEN>"
}

Response JSON: Best matching code snippet, source repository URL, confidence score

📄 Article Plagiarism Detection
Endpoint: POST /check_article

Request JSON:
{
  "article_text": "Artificial Intelligence is transforming technology.",
  "tavily_api_key": "<YOUR_TAVILY_API_KEY>"
}

Response JSON: List of matched articles, similarity percentages, matched content, URLs

🔄 AI De-Plagiarizing / Paraphrasing
Endpoint: POST /deplagiarize

Request JSON (text mode):
{
  "input_text": "This is a sample sentence.",
  "mode": "text"
}


Request JSON (code mode):
{
  "input_text": "def add(a, b): return a + b",
  "mode": "code",
  "openrouter_api_key": "<YOUR_OPENROUTER_API_KEY>"
}


Response JSON: De-plagiarized text or code

🐍 Project Structure
BACKEND/
│
├── app.py                     # Main Flask app with all routes
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys, server config)
├── services/                  # API service modules
│   ├── websearch_service.py   # Tavily web search integration
│   └── ...                    # Other helper modules
├── models/                    # AI models loaders (SentenceTransformer, Parrot)
├── utils/                     # Utility functions (similarity calculations, text cleaning)
├── logs/                      # Optional logging output
└── tests/                     # Test scripts for API endpoints

🚀 Available Scripts
# Start development server
python app.py

# Optional: Run tests
pytest tests/

# Install dependencies
pip install -r requirements.txt

🐛 Troubleshooting:
Common Issues
API Key Errors
✅ Ensure .env file exists and API keys are correct
✅ Check API permissions and quotas
✅ Make sure backend server is running before frontend requests

Library Errors
✅ Upgrade pip and Python to latest stable version
✅ Ensure torch, transformers, and sentence-transformers are installed

🤝 Contributing:

🍴 Fork the repository:
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m "Add amazing feature")
Push to your branch (git push origin feature/amazing-feature)
Open a Pull Request

📄 License:
This project is licensed under the MIT License - see LICENSE
 file for details.

🙏 Acknowledgments:
Flask for web framework
Sentence Transformers for semantic similarity
Parrot for AI paraphrasing
GitHub API for code repository scanning
Tavily API for web article matching
OpenRouter for AI model access

<div align="center">
Made with ❤️ by the Plagiarism Detection Team
• [⭐ Star this repo](https://github.com/KOLLIJAYANTHESWAR/KOLLIJAYANTHESWAR-plagiarism-checker-backend) 
• [🐛 Report Bug](https://github.com/KOLLIJAYANTHESWAR/KOLLIJAYANTHESWAR-plagiarism-checker-backend/issues) 
• [💡 Request Feature](https://github.com/KOLLIJAYANTHESWAR/KOLLIJAYANTHESWAR-plagiarism-checker-backend/issues)

</div>