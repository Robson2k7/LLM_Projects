from openai import OpenAI
import gradio as gr
import os

# Pobiera klucz do API OpenAI ze zmiennej środowiskowej
client = OpenAI()

# Funkcja do rozpoznawania mowy (Whisper)
def transcribe(audio):
    with open(audio, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcript.text

# Funkcja do generowania odpowiedzi GPT-4
def chat_with_gpt(text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content

# Funkcja do zamiany tekstu na mowę (TTS)
def text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        input=text,
        voice="alloy"
    )
    audio_path = "response.mp3"
    with open(audio_path, "wb") as audio_file:
        audio_file.write(response.content)
    return audio_path

# Połączenie wszystkich funkcji
def voice_assistant(audio):
    text = transcribe(audio)  # Rozpoznanie mowy
    response = chat_with_gpt(text)  # Odpowiedź od GPT-4
    audio_response = text_to_speech(response)  # Konwersja na mowę
    return response, audio_response  # Zwracamy tekst i plik audio

# Interfejs w Gradio
iface = gr.Interface(
    fn=voice_assistant,
    inputs=gr.Audio(type="filepath"),
    outputs=[gr.Textbox(), gr.Audio()],
    title="Asystent Głosowy AI",
    description="Mów do mikrofonu, a AI odpowie głosowo!"
)

iface.launch()


