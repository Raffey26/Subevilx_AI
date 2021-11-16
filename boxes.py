import tkinter as tk
from PIL import Image,ImageTk 
from tkinter.constants import HORIZONTAL
from tkinter.ttk import *
from tkinter import *
from json import load
import time
import tkinter as tk
from tkinter.constants import HORIZONTAL
from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk

class Loading:
    def __init__(self):
        self.r=tk.Tk()
        self.r.geometry('500x250')
        self.r.title("Loading")
        #text
        logo1=Image.open('D:\\AI graphics\\logobg.png')
        reslogobg=logo1.resize((500,250),Image.ANTIALIAS)
        newlogo1=ImageTk.PhotoImage(reslogobg)
        image_label1=tk.Label(image=newlogo1)
        image_label1.pack()
        a= Label(self.r,text="Loading...",bg="#54D7FD", fg="blue",font=("",15))
        a.place(x=190,y=15)

       
        #boxes
        for i in range(16):
            self.r.update()
            self.Playthat()
        
        self.r.mainloop()
        #making animation
    def Playthat(self):
        for i in range(20):
            for j in range(16):
                Label(self.r,bg="#FBFF01", width=2,height=1).place(x=(j+2)*25,y=135)
                time.sleep(1)
                self.r.update_idletasks()
                Label(self.r,bg="#FF9301", width=2,height=1).place(x=(j+2)*25,y=135)
            else:
                self.r.after(5000)
                self.r.destroy() 
                import aigraphics    

Loading()