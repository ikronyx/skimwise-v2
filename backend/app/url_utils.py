import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Extract visible text from paragraphs
        paragraphs = soup.find_all('p')
        text = "\n".join(p.get_text() for p in paragraphs)
        return text.strip()
    except Exception:
        return ""
