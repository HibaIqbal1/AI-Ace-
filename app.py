import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import webbrowser

# =========================
# Load API Key
# =========================

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found in .env file")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)                               

# =========================
# Page Settings
# =========================

st.set_page_config(
    page_title="AI Ace",
    page_icon="🤖",
    layout="wide"
)

# =========================
# Theme
# =========================

st.markdown("""
<style>

.stApp{
    background-color:#FDEBD0;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background-color:#F5F5F5;
}

/* Title */
h1{
    color:#444444;
    text-align:center;
}

/* Prompt Suggestions dropdown */
div[data-baseweb="select"] > div{
    min-height:60px;
    border-radius:15px;
    border:2px solid #d9a15b;
    box-shadow:0 3px 10px rgba(0,0,0,.08);
    background:white;
    display:flex;
    align-items:center;     /* Vertical Center */
}

/* Selected text */
div[data-baseweb="select"] span{
    font-size:22px;
    font-weight:500;
    line-height:60px;
}

/* Dropdown arrow */
div[data-baseweb="select"] svg{
    width:22px;
    height:22px;
}

/* Hide the text cursor/caret inside the select box */
div[data-baseweb="select"] input{
    caret-color: transparent !important;
}

/* Optional: better dropdown options */
ul[role="listbox"]{
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Title
# =========================

st.markdown(
"""
<h1 style='text-align:center;'>🤖 AI Ace</h1>

<p style='text-align:center;
font-size:22px;
color:#555;'>
Your Personal AI Assistant
</p>
""",
unsafe_allow_html=True
)

# =========================
# Sidebar
# =========================

with st.sidebar:

    st.header("Quick Actions")

    if st.button("🌐 Open Google"):
        webbrowser.open("https://google.com")

    if st.button("▶ Open YouTube"):
        webbrowser.open("https://youtube.com")

    if st.button("💼 Open LinkedIn"):
        webbrowser.open("https://linkedin.com")

    if st.button("💬 Open WhatsApp"):
        webbrowser.open("https://web.whatsapp.com")

# =========================
# Prompt Suggestions
# =========================

st.subheader("💡 Prompt Suggestions")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "prompt" not in st.session_state:
    st.session_state.prompt = None

if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = "Select a prompt..."

suggestions = [
    "Explain Artificial Intelligence",
    "Generate LinkedIn Post",
    "Data Analyst Roadmap",
    "Play Sapphire"
]

if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = ""

prompt = None

def load_prompt():
    if st.session_state.selected_prompt != "Select a prompt...":
        st.session_state.prompt = st.session_state.selected_prompt

selected_prompt = st.selectbox(
    "",
    options=["Select a prompt..."] + suggestions,
    key="selected_prompt",
    on_change=load_prompt
)

prompt = st.session_state.prompt
    
# =========================
# Chat History
# =========================
st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# Chat Input
# =========================

user_prompt = st.chat_input("Ask AI Ace...")

if user_prompt:
    prompt = user_prompt
    st.session_state.prompt = None

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Commands

    if prompt.lower() == "open google":

        webbrowser.open("https://google.com")

        reply = "🌐 Opening Google"

    elif prompt.lower() == "open youtube":

        webbrowser.open("https://youtube.com")

        reply = "▶ Opening YouTube"

    elif prompt.lower() == "open linkedin":

        webbrowser.open("https://linkedin.com")

        reply = "💼 Opening LinkedIn"

    elif prompt.lower() == "open whatsapp":

        webbrowser.open("https://web.whatsapp.com")

        reply = "💬 Opening WhatsApp"

    elif prompt.lower().startswith("play "):

        song = prompt[5:].strip()

        youtube_url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"

        webbrowser.open(youtube_url)

        reply = f"🎵 Opening YouTube search for {song}"

    else:

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role":"system",
                        "content":"You are Hiba's AI Ace, a helpful personal assistant."
                    }
                ] + st.session_state.messages
            )

            reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append(
    {
        "role":"assistant",
        "content":reply
    }
)
st.session_state.prompt = None




