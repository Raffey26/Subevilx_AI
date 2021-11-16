from json import load
import time
import tkinter as tk
from tkinter.constants import HORIZONTAL
from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import datetime
from time import strftime



root=tk.Tk()
root.title("SUBEVILX ASSISTANT")
root.geometry('500x250')
root.iconbitmap('D:\\AI graphics\\transparent bg black.ico')

#logo
logo=Image.open('D:\\AI graphics\\logobg.png')
reslogo=logo.resize((500,250),Image.ANTIALIAS)
newlogo=ImageTk.PhotoImage(reslogo)
image_label=tk.Label(image=newlogo)
image_label.pack(pady=0,padx=0)

r= sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 196)
engine.setProperty('volume', 2.7)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone()as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        listening=tk.Button(root,text="Litsening...",bg='#0303fc',width=10,height=1,fg='#FF001F',borderwidth=5)
        listening.place(x=200,y=170)

        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        query=query.lower()
        print(f"user said: {query}\n")
        root.update()
        e=tk.Entry(root,width=80,bg="#00FFCD",fg="#4200FF",borderwidth=5)
        e.insert(0,"User Said: "+ query)
        e.place(x=0,y=200)
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary (query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube"in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("youtube.com")
        elif "open google"in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("google.com")
        elif "open stack overflow"in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("stackoverflow.com")
        elif "play music"in query:
            import music
        elif "open facebook"in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("facebook.com")
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {strTime}")
            print(strTime)
            def time():
                 hello=strftime("%H:%M:%S %p")
                 label.config(text=hello)
            label=Label(root,font=("digital-7",30),fg="cyan", bg="black")
            label.place(x=160,y=34)
            time()
            root.update()


        elif"open code " in query:
            codepath="C:\\Users\\dawood\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif"open team " in query:
            teampath="C:\\Program Files\\TeamViewer\\TeamViewer.exe"
            os.startfile(teampath)
        elif "hello" in query:
            speak(f"hey there! . how can i help you?")

    except Exception as e:
        print("say that again please...")
        return "none"
    return query


#button
speaking=tk.Button(root,text="Speak Now",command=takeCommand,borderwidth=5,width=20,bg="#00FFCD",fg="#4200FF")
speaking.place(x=165, y= 135)
exit_but=tk.Button(root,text="Exit",command=root.quit, bg="#0303fc",fg="#FF001F")
exit_but.place(x=240,y=225)
root.mainloop()