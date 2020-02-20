#bibliotecas
from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import ttk
from time import ctime
import time
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import playsound
import random
from gtts import gTTS

#como a Verna fala com você
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='pt-br')

    r = random.randint(1,1000000)
    audio_file = f'audio-{str(r)}.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

#como você fala com a Verna
def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)

        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='pt-br')
        except sr.UnknownValueError:
            record_audio()
        except sr.RequestError:
            speak('O servidor está desligado')
        return voice_data

#ações
def GoogleSearch():
    search = record_audio('o que você quer que eu procure?')
    url = f'https://google.com/search?q={str(search)}'
    webbrowser.get().open(url)
    speak(f'ok, procurando por {search}')

def Maps():
    location =  record_audio('qual local você deseja encontrar?')
    url = f'https://google.nl/maps/place/{str(location)}'
    webbrowser.get().open(url)
    speak(f"aqui está, {str(location)} ")

def Yb():
    video = record_audio('o que você deseja ver?')
    url = f'https://youtube.com/search?q={video}'
    webbrowser.get().open(url)
    speak('boa escolha, abrindo...')

def calc():
    os.system('calc.exe')
    speak('abrindo calculadora')

def respond(voice_data):
    if 'seu nome' in voice_data:
        speak('olá eu sou verna')
    elif 'tempo atual' in voice_data:
        speak(time.localtime())
    elif 'horas' in voice_data:
        speak(time.localtime())
    elif 'pesquise' in voice_data:
        GoogleSearch()
    elif 'procure' in voice_data:
        GoogleSearch()
    elif 'procurar' in voice_data:
        GoogleSearch()
    elif 'pesquisar' in voice_data:
        GoogleSearch()
    elif 'ache' in voice_data:
        Maps()
    elif 'encontre' in voice_data:
        Maps()
    elif 'ver' in voice_data:
        Yb()
    elif 'assistir' in voice_data:
        Yb()
    elif 'calcule' in voice_data:
        calc()
    elif 'calculadora' in voice_data:
        calc()
    elif 'fechar' in voice_data:
        speak('ok, até mais')
        sys.exit()
    elif 'sair' in voice_data:
        speak('ok, até mais')
        sys.exit()
    elif 'sentindo triste' in voice_data:
        speak('veja isto')
        webbrowser.get().open('https://www.youtube.com/watch?v=kdu1BMfL9Vg')
        speak('ou isso')
        webbrowser.get().open('https://www.youtube.com/watch?v=qxJU4PYuNP0')
        speak('isso vai funcionar, acredite em mim')
        webbrowser.get().open('https://www.youtube.com/watch?v=PppkNH3bKV4')
    else:
        speak('desculpe, não entendi')
    record_audio()

#inicializar
def task():
    speak('no que posso ajudar?')
    voice_data = record_audio()
    respond(voice_data)

#checa se você acionou
def hello_assistant(voice_data):
    if 'assistente' in voice_data:
        task()
    else:
        record_audio()

#fica sempre te ouvindo
while True:
    voice_data = record_audio()
    hello_assistant(voice_data)