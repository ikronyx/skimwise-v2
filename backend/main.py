from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from summarizer import summarize_text
from pdf_utils import extract_text_from_pdf
from url_utils import extract_text_from_url

app = FastAPI(title="Skimwise Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific domains for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize/pdf")
async def summarize_pdf(
    summary_type: str = Form(...),
    file: UploadFile = File(...)
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    contents = await file.read()
    text = extract_text_from_pdf(contents)
    if not text.strip():
        raise HTTPException(status_code=400, detail="No text found in PDF")

    summary = summarize_text(text, summary_type)
    return {"summary": summary}

@app.post("/summarize/url")
async def summarize_url(
    summary_type: str = Form(...),
    url: str = Form(...)
):
    text = extract_text_from_url(url)
    if not text.strip():
        raise HTTPException(status_code=400, detail="No text found at URL")

    summary = summarize_text(text, summary_type)
    return {"summary": summary}
