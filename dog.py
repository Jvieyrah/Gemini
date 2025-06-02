import google.generativeai as genai
import os



genai.configure(api_key=os.environ['GEMINI_API'])

model = genai.GenerativeModel("gemini-1.5-flash")

dog_image = genai.upload_file(
   path="cachorro_collie_acho.png"
)

prompt = (
   "Pode identificar a raça do cachorro da foto e me dar duas ou três frases de informações a respeito dele? "
   "De preferência, alguma curiosidade interessante em português, citando a fonte da informação e sempre de um jeito leve e interessante."
)
response = model.generate_content([dog_image, prompt])

print(response.text)

