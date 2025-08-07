
# Skimwise

**Skimwise** is a lightweight, full-stack AI web app that summarizes content from URLs using free and open-source tools. It’s built for students, journalists, researchers, and curious readers who want to save time by extracting meaningful summaries from long-form web content.

### 🌐 Live Demo

- **Frontend (Vercel):** [https://your-vercel-url.vercel.app](https://your-vercel-url.vercel.app)
- **Backend (Railway):** [https://your-railway-url.up.railway.app](https://your-railway-url.up.railway.app)

---

## 🔧 Tech Stack

### Frontend
- **React** (with Vite)
- **Tailwind CSS**
- **Deployed on [Vercel](https://vercel.com)** _(Free Tier)_

### Backend
- **FastAPI**
- **Sumy** (for summarization)
- **NLTK**
- **Deployed on [Railway](https://railway.app)** _(Free Tier)_

---

## 📦 Features

- ✅ Paste a URL and get a clean summary
- ✅ Choose between summary types (e.g., LSA, Luhn, etc.)
- ✅ Simple, fast, and responsive interface
- ✅ All APIs are free to use — no paid APIs or accounts required

---

## 🚀 Getting Started

### Backend Setup

```bash
git clone https://github.com/your-username/skimwise.git
cd skimwise/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Download necessary NLTK tokenizer
python -c "import nltk; nltk.download('punkt')"

# Run FastAPI server
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

---

## 📁 Folder Structure

```
skimwise/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── summarizer.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── components/
```

---

## 🌍 Deployment Notes

- **Frontend (Vercel):**
  - Link the `frontend/` folder to a new Vercel project.
  - Set the environment variable `BACKEND_URL` to your Railway backend URL.

- **Backend (Railway):**
  - Deploy the `backend/` folder as a FastAPI project.
  - Make sure NLTK's `punkt` tokenizer is downloaded before starting the app.

---

## 🆓 100% Free & Open Source

This project uses **only free tools**:
- Open-source summarization (Sumy)
- Free-tier cloud services (Vercel, Railway)
- No API keys or third-party charges

---

## 📄 License

MIT License — use it freely and improve upon it!

---

## ✨ Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Sumy](https://github.com/miso-belica/sumy)
- [NLTK](https://www.nltk.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Vercel](https://vercel.com)
- [Railway](https://railway.app)
