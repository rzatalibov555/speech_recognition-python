import speech_recognition as sr
import os
import sys
import webbrowser
from gtts import gTTS

def talk(words):
    print(words)
    os.system("say:" + words)
    
talk("Привет! Cпроси у меня что-либо")

def command():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        
        audio = r.listen(source)
    
    with open("recodedaudio.wav","wb") as f:
        f.write(audio.get_wav_data())  
        
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
        
    
        
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()
    
    
    return zadanie
    
def makeSomething(zadanie):
    
    if "open site" in zadanie:
        talk("Уже открываю")
        url = "https://www.youtube.com/@sethub3879"
        webbrowser.open(url)    
    elif "stop" in zadanie:
        talk("Да конечно, без проблем.")
        sys.exit()
    elif "what's your name" in zadanie:
        talk("Меня зовут искусственный интеллект RzaSystem.")
    
    elif "открой мой youtube канал" in zadanie:
        talk("Уже открываю")
        url = "https://www.youtube.com/@sethub3879"
        webbrowser.open(url)
    elif "стоп" in zadanie:
        talk("Да конечно, без проблем.")
        sys.exit()    
    
        

while True:
    makeSomething(command())
        