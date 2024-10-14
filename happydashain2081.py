from pathlib import Path
import json
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Happy Dashain", page_icon="🤩")

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "happy_dashain.json"

def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)



lottie_coding = load_lottie_animation(LOTTIE_ANIMATION)
st.markdown("""
    <style>
        .main {
            background-color:#61dafb;
        }
    </style>
    """, unsafe_allow_html=True)

st_lottie(lottie_coding, height=300, key="coding")

def run_snow_animation():
    rain(emoji='❤️', font_size=20, falling_speed=5, animation_length="infinite")

st.markdown("""
    <style>
        .reportview-container {}
        .header {
            color: #ff6347;
            text-align: center;
             font-size: 3em;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
        .reportview-container {}
        .subheader {
            text-align: center;
             font-size: 2em;
        }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<h1 class="header">HAPPY BIJAYA DASHAMI 2081!!!!</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="subheader">MAY THIS DASHAIN GIVES YOU PROSPEROUS LIFE!!!!</h1>', unsafe_allow_html=True)

# Define CSS to style the bullet points
st.markdown("""
    <style>
        ul.custom-bullet li {
            list-style-type: square;
            color: #d33682;  /* Magneta Pink Colour */
            font-size: 2em
        }
    </style>
    """, unsafe_allow_html=True)



# Create a bulleted list with the custom class

st.markdown("""
    <ul class="custom-bullet">
        <li>MAY MY FAMILY BE MORE HAPPIER THAN BEFORE</li>
        <li>MAY NO DISEASES HARM MY FAMILY</li>
        <li>MAY THIS DASHAIN GIVES POWER TO CREATE STRONG MINDSET</li>
    </ul>
    """, unsafe_allow_html=True)

 
items = ["FATHER", "MOTHER", "BROTHER"]

# Create styled emoji bullets with reduced line spacing
emoji_bullets = "".join(f"<p style='color:#d33682; line-height:2.0;'>🌟 {item}</p>" for item in items)
st.markdown(emoji_bullets, unsafe_allow_html=True)

#items = [
 #   "MAY MY FAMILY BE MORE HAPPIER THAN BEFORE"
#]
#st.markdown("\n".join(f"- {item}" for item in items))   
#items = [
#   "MAY NO DISEASES HARM MY FAMILY"
#]
#st.markdown("\n".join(f"- {item}" for item in items))
#items= [
#        "MAY THIS DASHAIN GIVES POWER TO CREATE STRONG MINDSET"
#]
    #st.markdown("\n".join(f"- {item}" for item in items))


run_snow_animation()
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    img1 = Image.open("assets/image.jpeg")
    st.image(img1, caption="Happy Dashain Image 1", use_column_width=True)

with col2:
    img2 = Image.open("assets/image1.jpeg")
    st.image(img2, caption="Happy Dashain Image 2", use_column_width=True)




     

