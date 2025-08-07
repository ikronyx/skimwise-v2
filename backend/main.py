from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk

# Download both punkt and punkt_tab
for resource in ["punkt", "punkt_tab"]:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)

app = FastAPI()

# Allow only your frontend domain
origins = [
    "https://skimwise-v2.vercel.app",
    "https://skimwise-v2-bdl6.vercel.app",
    "https://skimwise-v2-d3ol15wuf-ikronyxs-projects.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # restrict to your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👋 Test endpoint
@app.get("/")
def hello():
    return {"message": "Hello from Skimwise backend!"}


# 🧠 Request model
class URLSummaryRequest(BaseModel):
    url: str
    summary_type: str = "Quick"  # placeholder for options like "Quick", "In-Depth", etc.


# 📄 Endpoint to summarize a URL
@app.post("/summarize/url")
def summarize_url(data: URLSummaryRequest):
    try:
        response = requests.get(data.url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join(p.get_text() for p in paragraphs)

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()

        # Choose number of sentences based on summary_type
        sentence_count = {
            "Quick": 3,
            "In-Depth": 7,
            "By Section": 5  # simple fallback
        }.get(data.summary_type, 3)

        summary = summarizer(parser.document, sentence_count)
        summary_text = "\n".join(str(sentence) for sentence in summary)

        return {
            "status": "success",
            "summary": summary_text
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
