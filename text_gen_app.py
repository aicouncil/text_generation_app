import streamlit as st
import google.generativeai as genai
import os

#configure api
api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)

#Create gemini model instance
model = genai.GenerativeModel('models/gemini-2.0-flash')

#Streamli UI
st.set_page_config(page_title="Our Generative text app powered by Gemini")
st.title("What do you want to know?")
st.markdown("Tell us what information do you want, I will provide you the details.")

#prompt input
prompt_input = st.text_input("Provide your prompt here", value="")

#Generate button
if st.button("Generate"):
    with st.spinner("Thinking...."):
        prompt = prompt_input.strip()
        try:
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as err:
            st.error(f"An error occured - {err}")
