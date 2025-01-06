import openai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.getenv("GITHUB_TOKEN")

if not api_key:
    raise ValueError("API key not found. Please set the 'GITHUB_TOKEN' environment variable.")

openai.api_key = api_key
openai.api_base = "https://models.inference.ai.azure.com"

def calculate_height(text):
    if not text:
        return 150
    num_lines = text.count('\n') + 1
    chars_per_line = 80
    num_wrapped_lines = sum(len(line) // chars_per_line + 1 for line in text.split('\n'))
    total_lines = max(num_lines, num_wrapped_lines)
    line_height = 24
    padding = 40
    return min(max(150, (total_lines * line_height) + padding), 500)

# Custom CSS for the new design
def apply_custom_css():
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
        }
        
        /* Title styling */
        h1 {
            color: #2D3748;
            font-size: 2.5rem !important;
            font-weight: 600 !important;
            margin-bottom: 2rem !important;
            text-align: center;
        }
        
        /* Input area styling */
        .stTextArea textarea {
            background-color: #F7FAFC !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 10px !important;
            padding: 1rem !important;
            font-size: 16px !important;
            min-height: 150px;
            resize: vertical;
        }
        
        /* Button styling */
        .stButton button {
            background-color: #818CF8 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 0.75rem 1.5rem !important;
            width: 100% !important;
            font-weight: 500 !important;
            border: none !important;
            margin-top: 1rem !important;
            transition: background-color 0.3s ease !important;
        }
        
        .stButton button:hover {
            background-color: #6B7CFF !important;
        }
        
        /* Output section styling */
        .output-text {
            background-color: #F7FAFC;
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            border: 1px solid #E2E8F0;
        }
        
        /* Label styling */
        label {
            color: #4A5568 !important;
            font-size: 1rem !important;
            margin-bottom: 0.5rem !important;
        }
        
        /* Remove default Streamlit padding */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
            max-width: 800px !important;
        }
        
        /* Spinner styling */
        .stSpinner {
            text-align: center;
            color: #818CF8 !important;
        }
        
        /* Error and warning styling */
        .stAlert {
            background-color: #FEF2F2;
            color: #DC2626;
            border-radius: 8px;
            border: 1px solid #FCA5A5;
        }
        
        .stWarning {
            background-color: #FFFBEB;
            color: #D97706;
            border-radius: 8px;
            border: 1px solid #FCD34D;
        }
        </style>
    """, unsafe_allow_html=True)

def grammar_checker():
    st.title("Sinhala Grammar Checker")

    if "grammar_messages" not in st.session_state:
        st.session_state.grammar_messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant. Correct incorrect Sinhala grammar in sentences. Ensure that sentences starting with 'මම' end with 'මි' and sentences starting with 'අපි' end with 'මු'. Only return the corrected sentences without any additional suggestions or explanations."
            }
        ]

    st.markdown("Enter your text:")
    
    current_text = st.session_state.get('grammar_input', '')
    height = calculate_height(current_text)
    
    user_input = st.text_area(
        "",
        key="grammar_input",
        label_visibility="collapsed",
        height=height
    )

    if st.button("Check Grammar", key="grammar_check"):
        if user_input.strip():
            try:
                with st.spinner("Checking..."):
                    response = openai.ChatCompletion.create(
                        model="gpt-4o",
                        messages=st.session_state.grammar_messages + [{"role": "user", "content": user_input}],
                        temperature=1.0,
                        max_tokens=256,
                        top_p=1.0
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    if assistant_response.strip():
                        st.markdown("### Corrected Text:")
                        st.markdown(f'<div class="output-text">{assistant_response}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text to check.")

def spelling_checker():
    st.title("Sinhala Spelling Checker")

    if "spelling_messages" not in st.session_state:
        st.session_state.spelling_messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant. Identify and correct spelling errors in Sinhala sentences. Only return the corrected sentences without any additional suggestions or explanations."
            }
        ]

    st.markdown("Enter your text:")
    
    current_text = st.session_state.get('spelling_input', '')
    height = calculate_height(current_text)
    
    user_input = st.text_area(
        "",
        key="spelling_input",
        label_visibility="collapsed",
        height=height
    )

    if st.button("Check Spelling", key="spelling_check"):
        if user_input.strip():
            try:
                with st.spinner("Checking..."):
                    response = openai.ChatCompletion.create(
                        model="gpt-4o",
                        messages=st.session_state.spelling_messages + [{"role": "user", "content": user_input}],
                        temperature=1.0,
                        max_tokens=256,
                        top_p=1.0
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    if assistant_response.strip():
                        st.markdown("### Corrected Text:")
                        st.markdown(f'<div class="output-text">{assistant_response}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text to check.")

def main():
    st.set_page_config(
        page_title="Sinhala Language Tools",
        page_icon="✍️",
        layout="centered"
    )
    
    apply_custom_css()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a tool:", ["Spelling Checker", "Grammar Checker"])

    if page == "Grammar Checker":
        grammar_checker()
    elif page == "Spelling Checker":
        spelling_checker()

if __name__ == "__main__":
    main()