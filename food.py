import google.generativeai as genai
import os



genai.configure(api_key=os.environ['GEMINI_API'])

model = genai.GenerativeModel("gemini-1.5-flash")

food_plate = genai.upload_file(
   path="prato-de-comida.png"
)

prompt = "Pode identificar com cuidado o que é servido nesse prato e estimar grosseiramente as suas calorias?"
response = model.generate_content([food_plate, prompt])

print(response.text)

