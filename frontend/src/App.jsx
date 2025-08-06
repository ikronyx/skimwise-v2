import React, { useState } from "react";
import PdfUploader from "./components/PdfUploader";
import UrlInput from "./components/UrlInput";
import SummaryDisplay from "./components/SummaryDisplay";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || "http://127.0.0.1:8000";

export default function App() {
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [summaryType, setSummaryType] = useState("quick");

  const handlePdfSubmit = async (file) => {
    setLoading(true);
    setError("");
    setSummary("");
    const formData = new FormData();
    formData.append("file", file);
    formData.append("summary_type", summaryType);

    try {
      const res = await fetch(`${BACKEND_URL}/summarize/pdf`, {
        method: "POST",
        body: formData,
      });
      if (!res.ok) {
        throw new Error(`Error: ${res.statusText}`);
      }
      const data = await res.json();
      setSummary(data.summary);
    } catch (err) {
      setError(err.message || "Failed to summarize PDF");
    } finally {
      setLoading(false);
    }
  };

  const handleUrlSubmit = async (url) => {
    setLoading(true);
    setError("");
    setSummary("");

    const formData = new FormData();
    formData.append("url", url);
    formData.append("summary_type", summaryType);

    try {
      const res = await fetch(`${BACKEND_URL}/summarize/url`, {
        method: "POST",
        body: formData,
      });
      if (!res.ok) {
        throw new Error(`Error: ${res.statusText}`);
      }
      const data = await res.json();
      setSummary(data.summary);
    } catch (err) {
      setError(err.message || "Failed to summarize URL");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Skimwise — AI Document & Web Summarizer</h1>

      <div className="summary-type-selector">
        <label>
          <input
            type="radio"
            value="quick"
            checked={summaryType === "quick"}
            onChange={() => setSummaryType("quick")}
          />
          Quick Summary
        </label>
        <label>
          <input
            type="radio"
            value="in-depth"
            checked={summaryType === "in-depth"}
            onChange={() => setSummaryType("in-depth")}
          />
          In-Depth Summary
        </label>
      </div>

      <PdfUploader onSubmit={handlePdfSubmit} disabled={loading} />
      <UrlInput onSubmit={handleUrlSubmit} disabled={loading} />

      {loading && <p className="loading-text">Generating summary...</p>}
      {error && <p className="error-text">{error}</p>}

      <SummaryDisplay summary={summary} />
    </div>
  );
}
