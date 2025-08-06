import React, { useState } from "react";

export default function UrlInput({ onSubmit, disabled }) {
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!url.trim()) {
      alert("Please enter a URL.");
      return;
    }
    onSubmit(url.trim());
  };

  return (
    <form className="url-input" onSubmit={handleSubmit}>
      <input
        type="url"
        placeholder="Paste article URL here..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        disabled={disabled}
      />
      <button type="submit" disabled={disabled}>
        Summarize URL
      </button>
    </form>
  );
}
