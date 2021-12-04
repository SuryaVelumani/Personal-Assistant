import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#text to speech

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is 0 and 1")



#time

def time():
    speak("Current time is ")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

#time()

def google():
    speak("Opening Google")
    webbrowser.open('https://www.google.com/')

#date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is ")
    speak(day)
    speak(month)
    speak(year)

#date()

#wish

def wishme():
    hour=int(datetime.datetime.now().hour)

    if(hour>=0 and hour<12):
        speak("Good Morning ! ")

    elif(hour>=12 and hour<=16):
        speak("Good Afternoon ! ")

    elif(hour>16 and hour<20):
        speak("Good Evening ! ")

    else:
        speak("Good Night Sweat Dreams ! ")

#wishme()
#get input through mic and prints text

def getcommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . . ")
        r.pause_threshold = 1
        audio = r.record(source , duration=5)

    try:
        print("Recognizing . . . ")
        query = r.recognize_google(audio , language='en')
        print(query)
        speak(f"You Said {query}")

    except Exception as e:
        print(e)
        speak("Say again please . . .")
        return "None"

    return query.lower()

#getcommand()

if __name__ == '__main__':

    while True:
        query = getcommand().lower()

        if 'wikipedia' in query:
            speak("Serching wikipedia ")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            print(result)
            speak(result)

    #    elif 'good morning' or 'good afternoon' or 'good evening' in query:
    #        wishme()

        elif 'date' in query:
            date()

        elif 'time' in query:
            time()

        elif 'open Google' in query:
            speak("Opening Google")
            google()

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open LinkedIn' in query:
            webbrowser.open("https://www.linkedin.com/login")

        elif 'open google sign in' in query:
            webbrowser.open("https://accounts.google.com/ServiceLogin/signinchooser?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")



       # To end the program
        elif 'stop' in query:
            exit(0)

