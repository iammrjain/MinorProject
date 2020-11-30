#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as tmsg
from ttkthemes import ThemedTk

from googletrans import *
translator = Translator()
import speech_recognition as s
sr = s.Recognizer()

import pyttsx3
engine = pyttsx3.init()
#engine.say(trans.text)
engine.runAndWait()

import pytesseract
from PIL import Image

global root
root=ThemedTk(theme="plastik")  #try and use yaru,breeze, arc in place of plastik theme.Delete this comment ok.
root.geometry("800x650")
root.title("TRANSLATOR")
    
gotohomepage = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Homepage.png")).resize((300,60), Image.ANTIALIAS))
speechtotext = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Speech_to_Text.png")).resize((300,60), Image.ANTIALIAS))
texttospeech = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Text_to_Speech.png")).resize((300,60), Image.ANTIALIAS))
imagetotextspeech = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Image_to_Text_Speech.png")).resize((300,60), Image.ANTIALIAS))
spk = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Speak.png")).resize((140,40), Image.ANTIALIAS))
clr = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\clear.png")).resize((140,40), Image.ANTIALIAS))
savetodoc = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Save_to_Document.png")).resize((350,50), Image.ANTIALIAS))
hinditoeng = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Hindi_to_English.png")).resize((300,60), Image.ANTIALIAS))
engtoeng = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\English_to_English.png")).resize((300,60), Image.ANTIALIAS))
translate = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Translate.png")).resize((200,40), Image.ANTIALIAS))
browse = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\Browse.png")).resize((150,40), Image.ANTIALIAS))

backgroundimage = ImageTk.PhotoImage((Image.open(r"D:\MinorProject\Images\maxresdefault.jpg")).resize((800,800), Image.ANTIALIAS))

en =StringVar()
def trans():
    global speech
    x = en.get()
    translator = Translator()
    trans = translator.translate(x)
    speech = trans.text
    T.insert('end',speech)

def speak():
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()

def welcome():
    global frame1,backgroundimage
    frame1= ttk.Frame(root)
    frame1.place(x=0,y=0,width=800,height=800)
    
    bkimage=Image.open(r"D:\MinorProject\Images\maxresdefault.jpg")
    bkimage=bkimage.resize((800,800), Image.ANTIALIAS)
    backgroundimage=ImageTk.PhotoImage(bkimage)
    backgroundimagelabel=ttk.Label(frame1,image=backgroundimage)
    backgroundimagelabel.place(x=0,y=0)

    label1 =ttk.Label(frame1,text="Welcome To",foreground="skyblue",background="black",font=("Cooper Black",44))
    label1.place(x=220 , y=50)
    
    label2 =ttk.Label(frame1,text="Speech to Text",foreground="blue",background="black",font=("Cooper Black",40))
    label2.place(x=210 , y=130)
    
    label3 =ttk.Label(frame1,text="and",foreground="skyblue",background="black",font=("Cooper Black",40))
    label3.place(x=350 , y=190)
    
    label4 =ttk.Label(frame1,text="Text to Speech",foreground="blue",background="black",font=("Cooper Black",40))
    label4.place(x=210 , y=250)
    
    label5 =ttk.Label(frame1,text="Converter",foreground="skyblue",background="black",font=("Cooper Black",40))
    label5.place(x=270 , y=310)
    
    
    homebutton = ttk.Button(frame1,image = gotohomepage,command=homepage,width=30)
    homebutton.place(x=250 , y=520)
    root.mainloop()


def homepage():
    frame1.place_forget()
    global frame2
    frame2= ttk.Frame(root)
    frame2.place(x=0,y=0,width=800,height=800)
    backgroundimagelabel=ttk.Label(frame2,image=backgroundimage)
    backgroundimagelabel.place(x=0,y=0)

    heading = ttk.Label(frame2,text = "Homepage",foreground="skyblue",background="black",font=("Cooper Black",40))
    heading.place(x=280,y=50)

    label6 = ttk.Label(frame2,text="Choose your option",background='black',foreground="blue",font=("Cooper Black",40))
    label6.place(x=150 , y=130)

    button1= ttk.Button(frame2,image = speechtotext, command=stt,width=30)
    button1.place(x=270 , y=350)

    button2= ttk.Button(frame2,image = texttospeech, command=tts,width=30)
    button2.place(x=270 , y=250)
    
    button3= ttk.Button(frame2,image = imagetotextspeech, command=itts,width=30)
    button3.place(x=270 , y=450)
     
def stt():
    frame2.place_forget()
    global frame3
    frame3= ttk.Frame(root)
    frame3.place(x=0,y=0,width=800,height=800)
    backgroundimagelabel=ttk.Label(frame3,image=backgroundimage)
    backgroundimagelabel.place(x=0,y=0)

    def text():
        global audio
        sr = s.Recognizer()
        with s.Microphone() as m:
            audio = sr.listen(m)
    
        global query
        query = sr.recognize_google(audio,language='eng-in')
        print(query)
        T.insert('end',query)
    def save():
        print('writing on...\n')
        #print(query)    
        file1 = open(r"D:\MinorProject\SpeechToText.txt", "w")
        file1.write(x)
        file1.close()

    heading = ttk.Label(frame3,text = "Speech to Text",foreground="blue",background="black",font=("Cooper Black",40))
    heading.place(x=200,y=30)

    tb = ttk.Button(frame3,image = spk, command=text,width=35).place(x=90 , y=160)

    T = Text(frame3, height = 10, width =50)
    T.place(x=350 , y=150)

    clear = ttk.Button(frame3,image = clr,command=lambda:T.delete(1.0,"end"),width=35)
    clear.place(x=90 , y=270)

    std = ttk.Button(frame3,image = savetodoc,command=save,width=35)
    std.place(x=50 , y=450)

    bth = ttk.Button(frame3,image = gotohomepage, command=homepage,width=35).place(x=200 , y=550)

def tts():

    frame2.place_forget()
    global frame4,e

    frame4= ttk.Frame(root)
    frame4.place(x=0,y=0,width=800,height=800)
    backgroundimagelabel=ttk.Label(frame4,image=backgroundimage)
    backgroundimagelabel.place(x=0,y=0)


    heading = ttk.Label(frame4,text = "Text to Speech",foreground="blue",background="black",font=("Cooper Black",40))
    heading.place(x=200,y=30)
    en =StringVar()
    l = ttk.Label(frame4,text = "Enter Text",foreground="orange",background="black",font=("Cooper Black",20)).place(x=130 ,y=110)
    entry0 = ttk.Entry(frame4,textvariable = en).place(x=70 , y=150, height = 27, width = 270)

    
    def trans():
        global speech,x
        x = en.get()
        translator = Translator()
        trans = translator.translate(x)
        speech = trans.text
        T.insert('end',speech)

    def speak():
        engine = pyttsx3.init()
        engine.say(speech)
        engine.runAndWait()

    def speak2(datta):
        dat=datta
        engine = pyttsx3.init()
        for x in dat:
            engine.say(x)
            engine.runAndWait()

    def save():
        print('writing on...\n')
        #print(query)    
        file1 = open(r"D:\MinorProject\TextToSpeech.txt", "w")
        file1.write(x)
        file1.close()
        
        

    def filedatas():
        filename=filedialog.askopenfilename()
        file2=open(filename,"rt")
        file2.seek(0)
        data=file2.readlines()

        textbox2 = Text(frame4, height = 10, width = 45)
        textbox2.place(x=400 , y=400)
        textbox2.delete(END)
        for x in data:
            textbox2.insert(END,x)    
        
        speakbutton = ttk.Button(frame4,image = spk,command=lambda:speak2(data),width=40).place(x=50 , y=490)
        labell=ttk.Label(frame4,text="File content",foreground="orange",background="black",font=("Cooper Black",20)).place(x=520 , y=360)

        cleartextbox2 = ttk.Button(frame4,image = clr,command=lambda:textbox2.delete(1.0,"end"),width=40)
        cleartextbox2.place(x=210 , y=490)
    
         
    tb = ttk.Button(frame4,image = translate, command=trans,width=20).place(x=100 , y=190)
    sb = ttk.Button(frame4,image = spk,command=speak,width=20).place(x=50 , y=260)
    tbb = ttk.Button(frame4,image = savetodoc, command=save,width=20).place(x=50 , y=320)

    T = Text(frame4, height = 10, width = 45)
    T.place(x=400 , y=150)
    l2 = ttk.Label(frame4,text = "Translated Text",foreground="orange",background="black",font=("Cooper Black",20)).place(x=490 ,y=320)
    
    clear = ttk.Button(frame4,image = clr,command=lambda:T.delete(1.0,"end"),width=20)
    clear.place(x=210 , y=260)
    bth = ttk.Button(frame4,image = gotohomepage, command=homepage,width=40).place(x=200 , y=570)
    choosebutton=ttk.Button(frame4,image = browse, command=filedatas,width=40).place(x=120 , y=420)
    
def itts():
    frame2.place_forget()
    global frame5
    frame5= ttk.Frame(root)
    frame5.place(x=0,y=0,width=800,height=800)
    backgroundimagelabel=ttk.Label(frame5,image=backgroundimage)
    backgroundimagelabel.place(x=0,y=0)

    heading = ttk.Label(frame5,text = "Image to Text/Speech",foreground="blue",background="black",font=("Cooper Black",40))
    heading.place(x=200,y=30)

    pth =StringVar()
    l = ttk.Label(frame5,text = "Enter Path",foreground="orange",background="black",font=("Cooper Black",20)).place(x=130 ,y=110)
    entry0 = ttk.Entry(frame5,textvariable = pth).place(x=70 , y=150, height = 27, width = 270)

    def convert():
        global abc
        y = pth.get()
        img = Image.open(y)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
        abc = pytesseract.image_to_string(img)
        T.insert('end',abc)
    
    def save():
        print('writing on...\n')
        #print(query)    
        file1 = open(r"D:\MinorProject\ImageToText.txt", "w")
        file1.write(abc)
        file1.close()


    tb = ttk.Button(frame5,image = translate, command=convert,width=35).place(x=90 , y=210)

    T = Text(frame5, height = 10, width =50)
    T.place(x=350 , y=150)

    clear = ttk.Button(frame5,image = clr,command=lambda:T.delete(1.0,"end"),width=35)
    clear.place(x=90 , y=270)

    std = ttk.Button(frame5,image = savetodoc,command=save,width=35)
    std.place(x=50 , y=450)

    bth = ttk.Button(frame5,image = gotohomepage, command=homepage,width=35).place(x=200 , y=550)

welcome()
root.mainloop()


# In[ ]:




