from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
#creating instance
root=Tk()

root.configure(background="white")

def function1():
    
    os.system("py takephoto.py")
    

    

def function2():

    os.system("py recognizer.py")
    playsound("sound.mp3")


   
def function3():

    root.destroy()


root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30),fg="black",bg="blue",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#first button
Button(root,text="Capture",font=("times new roman",20),bg="grey",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#third button
Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="grey",fg="black",command=function2).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)



Button(root,text="Exit",font=('times new roman',20),bg="black",fg="white",command=function3).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
