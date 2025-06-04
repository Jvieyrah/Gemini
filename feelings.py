import os
import time
import gradio as gr
import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument

# Configura a chave da API Gemini
genai.configure(api_key=os.environ["GEMINI_API"])

# Instrução inicial
initial_prompt = (
    "Você é uma inteligência virtual que pode receber e processar arquivos de vários tipos, "
    "como imagens, áudios, vídeos, textos e planilhas. Ao receber um arquivo, você deve analisá-lo, "
    "analisar os sentimentos e trazer uma estimativa em porcentagem dos sentimentos, além de fornecer "
    "uma análise adequada baseada no conteúdo."
)

# Instancia o modelo
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)
chat = model.start_chat()

# Upload e montagem dos arquivos
def upload_files(message):
    uploaded = []
    for file_path in message.get("files", []):
        uploaded_file = genai.upload_file(file_path)

        while uploaded_file.state.name == "PROCESSING":
            time.sleep(5)
            uploaded_file = genai.get_file(uploaded_file.name)
        uploaded.append(uploaded_file)
    return uploaded

# Monta o prompt com texto + arquivos
def assemble_prompt(message):
    prompt = [{"text": message["text"]}]
    prompt.extend(upload_files(message))
    return prompt

# Função principal do chat
def gradio_wrapper(message, _history):
    prompt = assemble_prompt(message)
    try:
        response = chat.send_message(prompt)
    except InvalidArgument as e:
        response = chat.send_message(
            "Houve um erro ao processar o arquivo enviado. Verifique se ele é compatível (imagem, texto, planilha, áudio ou vídeo) "
            "e tente novamente."
        )
    return response.text

# Interface Gradio
chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Chatbot com Análise de Sentimentos 🤖",
    multimodal=True
)

chat_interface.launch()
