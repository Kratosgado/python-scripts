import subprocess
import wolframalpha
import pyttsx3
# import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
# import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()
   
def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour >= 0 and hour < 12:
       speak("Good Morning!")
   elif hour >= 12 and hour < 18:
       speak("Good Afternoon!")
   else:
       speak("Good Evening!")
       
   assname =("Kratos 1 point o")
   speak("I am your Assistant")
   speak(assname)

def username():
    speak("What should i call you sir? ")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("################################".center(columns)) 
    print("Welcome Mr.", uname.center(columns))
    print("################################".center(columns))
    
    speak("How can i help you, Sir")

def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 586)
    server.ehlo()
    server.starttls()
    
    # enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 201.7645350762593 
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google_cloud(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query
    
   
if __name__ == '__main__':
   clear = lambda: os.system('clear')
   
   # this function will clean any command before execution of this python file
   clear()
   wishMe()
   username()
   
   while True:
       query = takeCommand().lower()
       
       # all the commands said by the user will be stored here in 'query'
       # and will be converted to lower case for easily recognition of command
       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences = 3)
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           speak("Here you go to youtube\n")
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           speak("Here you go to Google\n")
           webbrowser.open("google.com")