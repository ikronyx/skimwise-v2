import React, { useState } from "react";

export default function PdfUploader({ onSubmit, disabled }) {
  const [fileName, setFileName] = useState("");

  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setFileName(e.target.files[0].name);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const fileInput = e.target.elements.fileInput;
    if (fileInput.files.length === 0) {
      alert("Please select a PDF file.");
      return;
    }
    onSubmit(fileInput.files[0]);
  };

  return (
    <form className="pdf-uploader" onSubmit={handleSubmit}>
      <label htmlFor="fileInput" className="file-label">
        {fileName || "Choose a PDF file..."}
      </label>
      <input
        type="file"
        id="fileInput"
        name="fileInput"
        accept="application/pdf"
        onChange={handleFileChange}
        disabled={disabled}
      />
      <button type="submit" disabled={disabled}>
        Summarize PDF
      </button>
    </form>
  );
}
