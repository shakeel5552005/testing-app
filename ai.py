import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
#model = genai.GenerativeModel("gemini-2.5-flash-lite")
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Say Hello")

print(response.text)