import React from "react";

export default function SummaryDisplay({ summary }) {
  if (!summary) return null;

  // Split summary by lines (each bullet point)
  const lines = summary.split("\n");

  return (
    <div className="summary-display">
      <h2>Summary</h2>
      <ul>
        {lines.map((line, idx) => (
          <li key={idx}>{line.replace(/^•\s*/, "")}</li>
        ))}
      </ul>
    </div>
  );
}
