import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
#from wikipedia import summary

#Ignoring warning messages
warnings.filterwarnings('ignore')

# Record audio and return audio as a string

def recordAudio():

    #Record the audio
    r=sr.Recognizer()
    #creating a recognizer object

    #open mic and record
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    #use google's speech recognition
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said :  "+data)

    except sr.UnknownValueError:#check for unknown error
        print("Google speech recognition could not understand the audio")

    except sr.RequestError as e:
        print("Request result from google speech recognition service error")

    return data

#recordAudio()

#Text to audio function
def assistantResponse(text):
    print(text)
    
    #convert text to speech
    
    myobj = gTTS(text=text, lang='en', slow=False)
    
    #save converted audio to a file    
    myobj.save('assistant_response.mp3')
    
    #play the converted file
    os.system('start assistant_response.mp3')

#text='this is a test'
#assistantResponse(text)

#function for wake word(s) or phrase
def wakeWord(text):
    WAKE_WORDS={'computer','okay computer'}  #list of wakewords
    
    text=text.lower()  #convert text to all lowercase
    
    #check of user comand has wake words
    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #if no wakeword found in text from the loop
    return False

# A function to give date
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()] #e.g.Friday
    monthNum=now.month
    dayNum=now.day

    #a list of months
    month_names=['January','Frebruary','March','April','May','June','July','August','September','October',
                 'November','December']

    #a list of ordinal numbers
    ordinalNumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th',
                    '14th', '15th', '16th', '17th', '18th','19th','20th','21st','22nd','23rd','24th',
                    '25th', '26th', '27th', '28th','29th','30th','31st']



    return 'Today is ' +weekday+' '+month_names[monthNum-1]+' the '+ordinalNumbers[dayNum-1]+' . '

#print(getDate())

# function for random greeting


def greeting(text):

    #greeting inputs
    GREETING_INPUTS=['hi','hey','hello','hola','wassup']

    #greeting responses back
    GREETING_RESPONSES = ['howdy','whats good','hello','hey there']

    #if the user input is greeting then return a randomly chooen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)+'.'

    #if no greeting detected then return an empty string
    return ''

#function to get a person's first and last name from the text


def getPerson(text):
    wordList = text.split()  #split text into list of words

    for i in range(0, len(wordList)):
        if i+3 <= len(wordList)-1 and wordList[i].lower == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+wordList[i+3]

while True:
    #record audio
    text = recordAudio()
    response = ''

#check for wakeword
    if (wakeWord(text) == True):
        
        # check for greetings
        response = response + greeting(text)
        
        #check if user said anythong about date
        if ('date' in text) :
            get_date = getDate()
            response = response + ' ' + get_date
            
        #chack if user say who is
        if ('who is' in text):
            person = getPerson(text)
            #person = "LeBron James"
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

    #have the assistant respond back in audio

        assistantResponse(response)
