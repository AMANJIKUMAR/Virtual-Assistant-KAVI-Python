import speech_recognition as sr
import pyttsx3



listener = sr.Recognizer()
engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def talk('text'):
         engine.say(text)
         engine.runAndWait()

def talk_command()
try:

    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'kavi' in command:
            command = command.replace('kavi', '')

         print(command)
except:

    pass
    return command

def run_kavi():
    command = take_command()
    print(command)
    if 'play' in command:
        talk('playing')
        print('playing')



    run_kavi()

    #15.01