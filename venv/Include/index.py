import pyttsx3
import speech_recognition as sr
import os
import sys
import webbrowser
from gtts import gTTS

engine = pyttsx3.init()

r = sr.Recognizer()
r.pause_threshold = 1



# ===================================================
def talk(words):
    print(words)
    os.system("say:" + words)
    
talk("Hi! tell something")
# ===================================================





# ===================================================
def command():
   
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(source=mic, duration=1)
        audio = r.listen(source=mic)
        query = r.recognize_google(audio_data=audio).lower()
        
    # with open("recodedaudio.wav","wb") as f:
    #     f.write(query.get_wav_data())  
        
    try:
        # zadanie = r.recognize_google(mic, language="ru-RU").lower()
        zadanie = r.recognize_google(audio).lower()
        
        print("You said: " + zadanie)
        engine.say(zadanie)
        engine.runAndWait()
        
        print(command())
        
    except sr.UnknownValueError:
        talk("I dont understand")
        zadanie = command()
    
    
    return zadanie
# ===================================================

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
        talk("Sure. No problem.")
        sys.exit()    
    elif "new task":
        create_task()
        

 





def create_task():
    print("Add new task...")
    engine.say("Add new task...")
    engine.runAndWait()
    
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(source=mic, duration=1)
        audio = r.listen(source=mic)
        query = r.recognize_google(audio_data=audio).lower()
    
    # for create todo list
    with open("todo_list.txt", 'a') as file:
        file.write(f"{query}\n")
    
    # with open("recodedaudio.wav","wb") as file:
    #     file.write(f"{query.get_wav_data()}\n")
        
    engine.say(f"Task {query} added to todo list.")
    engine.runAndWait()
    print(f"Task {query} added to todo list.")
    
    

while True:
    makeSomething(command())
    