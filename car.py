import google.generativeai as genai
import os



genai.configure(api_key=os.environ['GEMINI_API'])

model = genai.GenerativeModel("gemini-1.5-flash")

image1 = genai.upload_file(
     path="a.jpeg"
)

prompt = "Identifique na foto o modelo do veiculo, cor, placa, se for possivel ver os ocupantes, identifique quantos ocupantes estão visiveis, o genero e idade do motorista e dos passageiros"
response1 = model.generate_content([image1, prompt])

print(response1.text)

image2 = genai.upload_file(
     path="b5.jpg"
)

response2 = model.generate_content([image2, prompt])

print(response2.text)

