import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./GrammerChecker.css";

const GrammarChecker = () => {
  const [paragraph, setParagraph] = useState("");
  const [, setSpellingCorrection] = useState("");
  const [grammarCorrection, setGrammarCorrection] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleCheck = async () => {
    if (!paragraph.trim()) {
      setError("Please enter text to check");
      return;
    }

    setIsLoading(true);
    setError("");
    setSpellingCorrection("");
    setGrammarCorrection("");

    try {
      const response = await fetch("http://localhost:8080/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ paragraph }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setSpellingCorrection(data.spelling_correction);
      setGrammarCorrection(data.grammar_correction);
    } catch (error) {
      console.error("Failed to fetch:", error);
      setError("Failed to check text. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(grammarCorrection).then(() => {
      alert("Corrected grammar text copied to clipboard!");
    });
  };

  const handleDownload = () => {
    const element = document.createElement("a");
    const file = new Blob([grammarCorrection], { type: "text/plain" });
    element.href = URL.createObjectURL(file);
    element.download = "corrected_grammar.txt";
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  return (
    <div className="grammar-checker">
      <div className="background-shapes">
        <div className="shape shape-1"></div>
        <div className="shape shape-2"></div>
        <div className="shape shape-3"></div>
      </div>

      <div className="checker-container">
        <Link to="/" className="back-button">
          ← Back to Home
        </Link>

        <div className="checker-content">
          <h1 className="checker-title">Sinhala Grammar Checker</h1>

          <div className="input-section">
            <label className="input-label">Enter your text:</label>
            <textarea
              className="text-input"
              value={paragraph}
              onChange={(e) => setParagraph(e.target.value)}
              placeholder="Enter Sinhala text to check grammar and spelling..."
              rows={6}
            />
            {error && <div className="error-message">{error}</div>}
            <button 
              onClick={handleCheck} 
              className="check-button"
              disabled={isLoading}
            >
              {isLoading ? "Checking..." : "Check Text"}
            </button>
          </div>

          {grammarCorrection && (
            <div className="results-section">
              <div className="correction-box">
                <h3 className="correction-title">Corrected Grammar Text</h3>
                <div className="correction-content">
                  {grammarCorrection || "No grammar corrections needed"}
                </div>
                <br />
                <div className="action-buttons">
                  <button className="action-button" onClick={handleCopy}>
                    Copy Text
                  </button>
                  <button className="action-button" onClick={handleDownload}>
                    Download Text
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default GrammarChecker;