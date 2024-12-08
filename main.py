from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerationConfig, GenerativeModel
import os
import vertexai
import streamlit as st

load_dotenv()

project_id = os.getenv("project_id")
region = os.getenv("region")

vertexai.init(project=project_id, location=region)


def user_interfaces():
    st.set_page_config("VertexAI Demo")
    st.header("Gemini on VertexAI")

    user_question = st.text_input("Ask me anything ?")
    if st.button("Generate"):
        model=GenerativeModel("gemini-1.0-pro")

        response = model.generate_content(user_question, stream=True)

        for res in response:
            st.write(res.text)


if __name__ == "__main__":
    user_interfaces()