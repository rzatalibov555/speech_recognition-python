import speech_recognition
import sys
import pyttsx3
engine = pyttsx3.init()

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1

def greeting():
    
    return "hi man"


def create_task():
    print("Add new task...")
    engine.say(query)
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=1)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio).lower()
    
    # for create todo list
    with open("todo_list2.txt", 'a') as file:
        file.write(f"{query}\n")
    return f"Task {query} added to todo list."

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio).lower()
    
    engine.say(query)
    engine.runAndWait()

if query == "yes":
    print(greeting())
elif query == "new task":
    print(create_task())
elif query == "finish":
    print("Sure. No problem.")
    sys.exit()
else:
    print("I dont understant you.")