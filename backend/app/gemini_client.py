import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt: str):
    model = genai.GenerativeModel("gemini-flash-latest")
    response = model.generate_content(prompt)
    return response.text

