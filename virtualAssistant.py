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

#how the verna talks to you
def speak(audio_string):
    tts = gTTS(text=audio_string, lang ='en')

    r = random.randint(1,1000000)
    audio_file = f'audio-{str(r)}.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

#how you talks to verna
def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)

        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Did not get that')

        except sr.RequestError:
            speak('Server is Down, sorry')
        return voice_data

#actions
def respond(voice_data):
    if 'name' in voice_data:
        speak('hi, my name is verna')
    elif 'current time' in voice_data:
        speak(ctime())
    elif 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = f'https://google.com/search?q={str(search)}'
        webbrowser.get().open(url)
        speak(f'ok, searching for {search}')
    elif 'find location' in voice_data:
        location =  record_audio('which location you want to search for')
        url = f'https://google.nl/maps/place/{str(location)}'
        webbrowser.get().open(url)
        speak("heres is your location"+str(location)+"&/amp;")
    elif 'watch' in voice_data:
        video = record_audio('what do you want to watch')
        url = f'https://youtube.com/search?q={video}'
        webbrowser.get().open(url)
        speak('good choice, opening')
    elif ('calculate' or 'calculator') in voice_data:
        os.system('calc.exe')
        speak('opening calculator')
    elif 'exit' in voice_data:
        speak('ok bye')
        root.destroy()
    elif 'feeling sad' in voice_data:
        speak('try watch this')
        webbrowser.get().open('https://www.youtube.com/watch?v=kdu1BMfL9Vg')
        speak('or this')
        webbrowser.get().open('https://www.youtube.com/watch?v=qxJU4PYuNP0')
        speak('this will work, trust me')
        webbrowser.get().open('https://www.youtube.com/watch?v=PppkNH3bKV4')
    else:
        speak('sorry, did not get that')

#init
def task():
    speak('can i help you')
    voice_data = record_audio()
    respond(voice_data)

#screen definition
root = tk.ThemedTk()
root.get_themes()
root.set_theme("scidblue")
root.resizable(100,100)
root.configure(background="white")
root.title("Verna, the Assistant")

#buttons
task_btn = ttk.Button(root,text="Talk w/ Verna",command=task,width=50).grid(row=0,column=0,ipady=20,ipadx=90)
save_btn = ttk.Button(root,text="Exit",command=root.destroy,width=50).grid(row=1,column=0,ipady=20,ipadx=90)

#screen init
root.mainloop()