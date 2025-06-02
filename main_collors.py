import google.generativeai as genai
import os



genai.configure(api_key=os.environ['GEMINI_API'])

model = genai.GenerativeModel("gemini-1.5-flash")

image = genai.upload_file(
     path="social_media_viagem.png"
)

prompt = "Crie uma tabela que lista as 10 cores principais de uma imagem, ordenado por porcentagem aproximada de presença da cor, sua referencia em cmyk, rgb e hexadecimal"
response = model.generate_content([image, prompt])

print(response.text)

