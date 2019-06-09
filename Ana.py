#     Imports                                                 !! Pls install all libs !!
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys


#defining engine
engine = pyttsx3.init("sapi5")
engine.setProperty('rate',130)

#Client for search
client = wolframalpha.Client('your client id goes here')
#setting up voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
#definations

def speak(audio): #audio spoken by comp
    print('A.I :- '+ audio)
    engine.say(audio)
    engine.runAndWait()

def greet(): #greeting by AI
    current_time = int(datetime.datetime.now().hour)
    if current_time >= 0 and current_time < 12:
        speak('Good Morning!')

    if current_time >= 12 and current_time < 16:
        speak('Good Afternoon!')

    if current_time >= 16 and current_time !=0:
        speak('Good Evening!')
def command(): #command given
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to your command.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language = "en-in")
        print("You:- "+ query +'\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query
def searchq(): #for searches query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say what to search Sir...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language = "en-in")
        print("You want to search this :- "+ query +'\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query

def sendEmail(to, content): #email configs
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'password')
    server.sendmail('yourmail@gmail.com', to, content)
    server.close()
    
#program begins
greet()
speak('Hello Sir, I am your digital assistant Ana. ')
speak('How may I help you?')

#main program
while True:
    query= command()
    query= query.lower()
#opening  websites
    if 'open google' in query:
        speak('okay')
        webbrowser.open('www.google.com')
    elif 'open youtube' in query:
        speak('okay')
        webbrowser.open('www.youtube.com')
    elif 'open gmail' in query:
        speak('okay')
        webbrowser.open('www.gmail.com')
    elif 'open yahoo' in query:
        speak('okay')
        webbrowser.open('www.yahoo.com')
    elif "what\'s up" in query or 'how are you' in query:
        msg = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(msg))
    elif 'abort' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
    elif 'play music' in query:
        music_dir = 'F:\\Music' # replace it with your directory 
        songs = os.listdir(music_dir)
        x=random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir, songs[x]))
        print('playing ' + songs[x])


#searching things
    
    elif 'search youtube' in query:
        speak('okay')
        webbrowser.open('https://www.youtube.com/results?search_query=' + searchq())
    elif 'search google' in query:
        speak('okay')
        webbrowser.open('https://www.google.com/search?q=' + searchq())



    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = command()
            to = "sendermail@gmail.com"    
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry sir . I am not able to send this email")


#using clients for search

    else:
        query = query
        speak('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('Google says - ')
                speak('Got it.')
                speak(results)
                    
            except:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('Wikipedia says - ')
                speak(results)
        
        except:
            webbrowser.open('www.google.com')
            speak('Try to search on Google Sir!')
            speak('I am unable to find it.')
        
    speak('Next Command! Sir!')
        
