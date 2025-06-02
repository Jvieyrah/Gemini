import google.generativeai as genai
import os
import gradio as gr

# Configurar chave da API
genai.configure(api_key=os.environ["GEMINI_API"])

# Definir sistema
initial_prompt = "Você é um consultor de desenvolvimento de projetos."

# Instanciar modelo e iniciar chat
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)
chat = model.start_chat()
def gradio_wrapper(message, _history):
   # Extraia o texto da mensagem
   prompt = [message["text"]]
   uploaded_files = []
   # Iterar sobre cada arquivo recebido
   if message["files"]:
     for file_gradio_data in message["files"]:
       print(file_gradio_data)
       # Obter o caminho local do arquivo
       file_path = file_gradio_data["path"]
       # Fazer upload do arquivo para o Gemini
       uploaded_file_info = genai.upload_file(file_path)
       # Adicionar o arquivo uploadado à lista
       uploaded_files.append(uploaded_file_info)
   prompt.extend(uploaded_files)
   # Envie o prompt para o chat e obtenha a resposta
   response = chat.send_message(prompt)
   return response.text

chat_interface = gr.ChatInterface(
   fn=gradio_wrapper,
   title="Chatbot com Suporte a Arquivos 🤖",
   multimodal=True
)
chat_interface.launch()
