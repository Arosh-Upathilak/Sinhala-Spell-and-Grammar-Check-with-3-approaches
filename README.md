# Sinhala Spell and Grammar Check with 3 Approaches

## Overview
This system is designed to perform Sinhala spell and grammar checking using three approaches:

1. **Rule-Based Model**: Applies predefined linguistic rules to detect and correct grammar errors.
2. **OpenAI Model**: Utilizes advanced AI models, such as GPT, to understand context and provide precise corrections.
3. **Machine Learning Model**: Leverages trained models on large datasets to identify and resolve spelling and grammatical errors.

The combination of these methods ensures robust and context-aware error correction for Sinhala text.

---

## Features
- Spell checking with fuzzy matching for misspelled words.
- Grammar correction using both rule-based and AI-powered techniques.
- User-friendly interface for text input and result display.

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/username/Sinhala-Spell-and-Grammar-Check.git
```

### 1. Rule-Based Model

#### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd Sinhala-Spell-and-Grammar-Check/backend
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend application:
   ```bash
   python app.py
   ```

#### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd Sinhala-Spell-and-Grammar-Check/frontend
   ```
2. Install the required dependencies:
   ```bash
   npm install
   ```
3. Start the frontend application:
   ```bash
   npm start
   ```

### 2. OpenAI Model Setup
1. Navigate to the OpenAI model directory:
   ```bash
   cd Sinhala-Spelling-corrector-and-Grammar-Checker-using-OpenAI
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your ChatGPT API key to the `.env` file:
   ```
   OPENAI_API_KEY=YOUR_GITHUB_TOKEN
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

### 3. Machine Learning Model Setup
1. Navigate to the Machine Learning model directory:
   ```bash
   cd Sinhala-Spell-and-Grammar-Check-using-ML-Model
  
   ```

---

## Additional Notes
- Ensure Python (version >= 3.8) and Node.js (version >= 14) are installed on your system.
- Use a virtual environment for the backend to manage Python dependencies effectively:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

---

## Contribution
Feel free to contribute to this project by submitting issues or pull requests. Ensure that your contributions adhere to the repository's guidelines.

For any inquiries, contact: [aroshupathilak@gmail.com](mailto:aroshupathilak@gmail.com)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
