import streamlit as st
from PIL import Image


st.title("Saathvik's Resume")
st.image('Saathvik's cv.png')




contact_form = """
<form action="https://formsubmit.co/shravyarinky29@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your em@il" required>
     <textarea name="message" placeholder="your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form , unsafe_allow_html=True)

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")



st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """

st.markdown(st_style , unsafe_allow_html=True)
