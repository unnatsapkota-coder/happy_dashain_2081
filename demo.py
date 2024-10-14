import streamlit as st
from streamlit_lottie import st_lottie
import json
from pathlib import Path

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "happy_dashain.json"

# Set the page configuration at the very top
st.set_page_config(page_title="Happy Dashain", page_icon="🤩")
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

animation = load_lottie_animation(LOTTIE_ANIMATION)
st.markdown("""
    <style>
        .left-container {
            display: flex;
            justify-content: flex-start;  /* Aligns content to the left */
        }
        .animation {
            width: 400px;  /* Adjust the size as needed */
        }
    </style>
    """, unsafe_allow_html=True)
from streamlit.components.v1 import html

# Embed the animation in a div with class "left-container"
html(f"""
    <div class="left-container">
        <lottie-player src='data:application/json;base64,{animation}' background="transparent" speed="1" class="animation" loop autoplay></lottie-player>
    </div>
    """, height=400)
