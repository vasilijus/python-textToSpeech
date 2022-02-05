
#import the libraries
from gtts import gTTS
from playsound import playsound
from tkinter import *

#initialized window
root = Tk()
root.geometry('600x300')
root.title('Speak out')
root.config(bg='white')

#Labels
Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)

# text variable
Msg = StringVar()

#Entry
input_field = Entry(root, textvariable=Msg, width = '60')
input_field.place(x=20, y=100)

#tts function
def tts():
    Message = input_field.get()
    speech = gTTS(text = Message)
    file = 'test.mp3'
    speech.save(file)
    playsound(file)

def Exit():
    root.destroy()
    
def Reset():
    Msg.set("")
    
#Buttons
Button(root, text = "PLAY" , font = 'arial 15 bold', command = tts, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = '#0059b3').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)

#infinite loop to run program
root.mainloop()