import google.generativeai as genai
import os



genai.configure(api_key=os.environ['GEMINI_API'])

model = genai.GenerativeModel("gemini-1.5-flash")

with open("curriculo-joao-silva.txt", "r") as file:
   curriculo = file.read()

prompt = f"Por favor, aprimore o meu currículo para deixá-lo mais assertivo e enfatizando os pontos positivos. Eis o meu currículo:\n{curriculo}"
response = model.generate_content(prompt)

print(response.text)

