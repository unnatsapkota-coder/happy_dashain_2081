from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain


THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "happy_dashain.json"

import json

def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    



def run_snow_animation():
    rain(emoji='❤️', font_size=20, falling_speed=5, animation_length="infinite")



    def get_person_name():
        query_params = st.experimental_get_query_params()
        return query_params.get("name",["Friend"])[0]
    


st.set_page_config(page_title="Happy Dashain", page_icon="🤩")


run_snow_animation()


with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_person_name():
    return "Your Name"
FAMILY = get_person_name()
st.header(f"Happy Holidays, {FAMILY}! 🤩🤩", anchor=False)
     

lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=300)


st.markdown(
    f"Dear {FAMILY}, wishing you a wonderful holiday season filled with joy and peace."
)