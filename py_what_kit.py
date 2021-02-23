import speech_recognition as sr
import pyttsx3
from email_bot import talk,get_info
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()

def Search():
    command=get_info()
    if 'play' in command:
        command=command.replace("play","")
        pywhatkit.playonyt(command)
    elif 'search' in command:
        command=command.replace("search","")
        pywhatkit.search(command)
    talk('Fuck You...')

if __name__=='__main__':
    while True:
        Search() 