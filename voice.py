#!/usr/bin/env python3                                                                                

import speech_recognition as sr 
import pyaudio

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)
    
'''
r = sr.Recognizer()
with sr.AudioFile("file.wav") as source:
    audio = r.record(source)
'''

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
'''
if your voice does not recognize
pip install --upgrade gcloud
pip install --upgrade google-api-python-client
'''
