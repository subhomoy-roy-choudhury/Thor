import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            talk('listening...')
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('anariboyz007@gmail.com', '75subho2096')
    email = EmailMessage()
    email['From'] = 'anariboyz007@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'subhomoy': 'subhomoyrchoudhury@gmail.com',
    'bts': 'subhomoyroychoudhury@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if send_more=='yes' :
        get_email_info()
    elif send_more=='no' :
        talk('Have a good Day')
        # exit()

if __name__=='__main__':
    while True:
        get_email_info()