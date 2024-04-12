import google.generativeai as genai
from apikey import GOOGLE_API_KEY
import os

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)