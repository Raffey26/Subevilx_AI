import tkinter
from tkinter import *
from time import strftime
# from tkinter import font


root= Tk()
root.title('clock')

def time():
    s=strftime("%H:%M:%S %p")
    label.config(text=s)
    label.after(1000,time)

label=Label(root,font=("digital-7",50),bg="black",fg="cyan")
label.pack(anchor="center")
time()
mainloop()
