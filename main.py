#!/usr/bin/env python3                                                                                
import requests
import speech_recognition as sr  
import sys 
import json
import html

debug = False

seconds_for_response = 20


url = "https://opentdb.com/api.php?amount=10&category=18"
questions = json.loads(requests.get(url).content.decode('utf8').replace("'",'"')).get("results")
questions = [q["question"] for q in questions]



if (debug):
    sys.exit()
# get audio from the microphone      

                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source: 
    for q in questions:                                                                      
        print(html.unescape(q))                                                                              
        audio = r.listen(source,10,seconds_for_response)   
        try:
            print("You said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

