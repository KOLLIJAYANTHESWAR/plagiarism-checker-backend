# 🔍 Advanced Plagiarism Detection Suite

<div align="center">

![Plagiarism Checker](https://img.shields.io/badge/AI-Plagiarism%20Detection-blue?style=for-the-badge&logo=search&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

### 🚀 AI-Powered Multi-Modal Plagiarism Detection Platform

Semantic text analysis • GitHub code similarity • Web article matching • Intelligent paraphrasing

</div>

---

## 📌 Project Overview

The **Advanced Plagiarism Detection Suite** is a modern AI-integrated platform designed to detect plagiarism across multiple content types using intelligent similarity analysis and real-time API integrations.

The system focuses on:

- Semantic text similarity detection
- GitHub repository-based code comparison
- Web-scale article plagiarism analysis
- AI-powered paraphrasing
- Real-time interactive UI feedback
- Secure client-side API integration

Built using the **Next.js 15 App Router architecture** with TypeScript and a scalable component system.

---

## 🏗️ System Architecture

```
User
  ↓
Next.js Frontend (App Router)
  ↓
API Integration Layer
  ↓
OpenRouter  |  GitHub API  |  Tavily API
  ↓
AI & Web Analysis Engines
  ↓
Structured Similarity Reports
```

---

## 🌟 Core Features

### 🔍 Text Plagiarism Detection
- AI-powered semantic similarity scoring
- Confidence-based result metrics
- Matched content highlighting
- Real-time character validation

---

### 💻 Code Plagiarism Scanner
- GitHub repository scanning
- Intelligent code comparison logic
- Repository reference linking
- Similarity confidence scoring

---

### 📄 Article Plagiarism Analysis
- Tavily-powered web search matching
- Large content handling (up to 10,000 words)
- Source-based comparison
- Web content confidence indicators

---

### 🔄 AI Paraphrasing Engine
- OpenRouter model integration
- Intelligent rewriting system
- Clean formatted output
- Side-by-side comparison view

---

## 🎨 User Experience

- 🌙 Dark / Light theme toggle
- 📱 Fully responsive layout
- ⚡ Real-time validation & feedback
- 📊 Interactive similarity indicators
- 🔐 Local API key management via settings panel
- 🎯 Clean modular component architecture

---

## 🛠️ Tech Stack

### Frontend
- Next.js 15 (App Router)
- React 18
- TypeScript 5
- Tailwind CSS
- Shadcn/UI

### AI & API Integrations
- OpenRouter (AI text analysis & paraphrasing)
- GitHub REST API (code scanning)
- Tavily API (web search intelligence)

### Tooling
- ESLint
- TypeScript strict mode
- PostCSS
- Tailwind configuration
- Modular component architecture

---

## 📦 Project Structure

```
plagiarism-checker-frontend/
│
├── app/                    # Next.js App Router
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
│
├── components/
│   ├── ui/                 # Shadcn/UI components
│   ├── theme-provider.tsx
│   ├── use-toast.ts
│   └── custom modules
│
├── public/
├── package.json
├── next.config.mjs
├── tailwind.config.ts
├── tsconfig.json
└── README.md
```

---

## ⚙️ API Configuration

The platform requires external API keys for full functionality.

### Required Services

| Service     | Purpose |
|-------------|----------|
| OpenRouter  | AI text similarity & paraphrasing |
| GitHub API  | Code repository scanning |
| Tavily API  | Web article search & matching |

You can configure keys via:

- Settings Panel (Recommended)
- `.env.local` (Development only)

Example:

```
NEXT_PUBLIC_OPENROUTER_API_KEY=your_key
NEXT_PUBLIC_GITHUB_TOKEN=your_token
NEXT_PUBLIC_TAVILY_API_KEY=your_key
```

---

## 🚀 Running Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/plagiarism-checker-frontend.git
cd plagiarism-checker-frontend
```

### 2️⃣ Install Dependencies

```bash
npm install
```

### 3️⃣ Start Development Server

```bash
npm run dev
```

Application runs at:

```
http://localhost:3000
```

---

## 🔧 Available Scripts

```bash
npm run dev
npm run build
npm run start
npm run lint
npm run type-check
```

---

## 🔐 Security Notes

- API keys stored locally (development mode only)
- Input validation before API calls
- Error boundary handling
- No hardcoded secrets
- Production deployment should use a backend proxy

---

## 🎯 Engineering Highlights

✔ Multi-modal plagiarism detection  
✔ Semantic AI similarity scoring  
✔ GitHub code scanning integration  
✔ Web content intelligence via Tavily  
✔ Modular scalable UI architecture  
✔ Type-safe TypeScript implementation  
✔ Production-ready Next.js structure  

---

## 📈 Future Enhancements

- Backend proxy server for secure API calls
- User authentication & dashboard
- Exportable plagiarism reports (PDF)
- Persistent report history
- AI model comparison mode
- Cloud deployment (Vercel / AWS)

---

## 🤝 Contributing

1. Fork the repository  
2. Create feature branch  
3. Commit changes  
4. Push to branch  
5. Open Pull Request  

---

## 📄 License

MIT License — Free for learning and portfolio use.

---

## 👨‍💻 Author

**Kolli Jayanth Eswar**

Full-Stack & AI Systems Developer  
Next.js | TypeScript | AI Integration | Modern Web Systems
