import speech_recognition 
import pyttsx3
import random
import os
import webbrowser

engine = pyttsx3.init()

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1


commands_dict = {
    'commands':{
        'new_task':["create new task","new", "task","novaya zametka","new tusk", "new task"],
        'play_Random_Music':["music","random music"],
        'open_youtube_channel':["sethub","youtube","my channel","open my youtube channel"],
    }
}





# DEF ZONE

def listen_command():
    try:
        # prosluwivanie mikrafona
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=1)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio).lower()
            
        return query
        # prosluwivanie mikrafona
    except speech_recognition.UnknownValueError:
        return "I dont understand you man."

# ----------------------------------------------------

def open_youtube_channel():
    engine.say("Welcome to my channel!")
    engine.runAndWait()
    url = "https://www.youtube.com/@sethub3879"
    webbrowser.open(url)

# ----------------------------------------------------

def new_task():
    print("What you want add to list?")
    engine.say("What you want add to list?")
    engine.runAndWait()
    
    query = listen_command()
    
    # sazdat fayl dlya zapisi
    with open("todo-list.txt", "a") as file:
        file.write(f'{query}\n')
    engine.say("task added to todo list.")
    engine.runAndWait()
    return f'The {query} task added to todo list.'
   
    # sazdat fayl dlya zapisi

# ----------------------------------------------------

def play_Random_Music():
    files = os.listdir('music') # music files directory   
    random_file = f'music/{random.choice(files)}'
    os.system(f'MediaPlayer {random_file}')

    return f'Playing: {random_file.split("/")[-1]}'
# ----------------------------------------------------


def main():
    # print(globals)
    query = listen_command()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]()) 
# DEF ZONE


if __name__ == '__main__':
    main()


    
    
    
    
    
    
    
