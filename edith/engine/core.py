import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import webbrowser
import psutil
import wikipedia
import pyautogui
import sys
import subprocess
import google.generativeai as genai
from engine.apikey import GOOGLE_API_KEY
import playsound as playsound
import pyjokes
import winshell
import eel


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

#@eel.expose
def username():
    '''speak("What should I call you")
    uname=takeCommand()
    speak("Welcome Mister "+ uname)''' 
    speak("Welcome Atharva How can i help you ?")

#@eel.expose
def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery= str(psutil.sensors_battery())
    speak("Battery is at"+ battery)
#@eel.expose
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am your virtual assistant Jarvis.")
#@eel.expose
def speak(audio) :
     eel.DisplayMessage(audio)
     engine.say(audio)
     print(audio)
     engine.runAndWait()
     
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


@eel.expose
def takeCommand():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listning....!")
       #eel.DisplayMessage("Listning....!")
       r.adjust_for_ambient_noise(source)
       audio = r.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
       print('recognizing')
       #eel.DisplayMessage('recognizing....')
       print("You said : " + r.recognize_google(audio))
       query=r.recognize_google(audio)
       #eel.DisplayMessage(query)
       time.sleep(2)
       #eel.ShowHood
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
       query=" "
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))
       query =" "
    return query

#@eel.expose
def search_querry(order) :
    search_url= f'https://www.google.com/search?q={order}'
    webbrowser.open_new_tab(search_url)

#@eel.expose
def cam():
 import tkinter
 from tkinter import messagebox
 import PIL.Image, PIL.ImageTk
 import time
 import cv2

 class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        self.vid = MyVideoCapture(self.video_source)
        self.canvas = tkinter.Canvas(window, height=self.vid.height, width=self.vid.width)
        self.canvas.pack()

        btn_frame = tkinter.Frame(window, background="Black")
        btn_frame.place(x=0, y=0)

        self.btn_snapshot = tkinter.Button(btn_frame, text="Snapshot", width=20, bg="black", fg="white", command=self.snapshot)
        self.btn_snapshot.pack(side="left", padx=10, pady=10)

        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("My Capture " + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            messagebox.showinfo("Notification", "Image Saved")

    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)

 class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None
        else:
            return ret, None

 App(tkinter.Tk(), "Camera")



#eel.expose
def note():
    speak("What should i write , sir?")
    note=takeCommand()
    file=open('jarvis.txt','w')
    speak("Sir, Should I include date and time as well?")
    sn=takeCommand()
    if 'yes' in sn or  'sure' in sn or 'yeah' in sn:
      strTime=datetime.now().strftime("%H:%M:%S")
      file.write (strTime)
      file.write(note)
      speak("Done Sir!")
    else:
      file.write(note)
      speak("Done Sir!")


#@eel.expose
def bmi():
    speak("Please tell your height in centimetres")
    height = takeCommand()
    speak("Please tell your weight in kilograms")
    weight = takeCommand()
    height = float(height)/100
    BMI = float(weight)/(height*height)
    speak("Your body mass index is " + str(BMI))
    if (BMI>0) :
        if(BMI<=16) :
            speak("You are severly underweight")
        elif (BMI<=18.5) :
            speak("You are underweight")
        elif (BMI<=25):
            speak("You are healthy")
        elif (BMI<=30) :
            speak("You are overwieght")
        else:
            speak("You are severly over weight")
    else:
        speak("Enter valid details")


#@eel.expose
def GEMINI_SEARCH(order):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(order)
    result = response.text
    result = result.replace('*','')
    print(result)
    speak(result)


#@eel.expose
def screenshot():
    speak('Sir, please tell me the name for this file.')
    name=takeCommand().lower()
    speak("please hold the screen")
    time.sleep(3)
    img=pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("screenshot captured sir!")


#@eel.expose
def shutdown():
    speak('Hold on a second sir! Your system is on itsa way to shutdown')
    speak('Make sure all of your applications are closed')
    time.sleep(5)
    subprocess.call(['shudown','/s'])


#@eel.expose
def locate():
    order = order.replace("where is"," ")
    location = order
    speak("Locating.....")
    speak(location)
    webbrowser.open("https://www.google.co.in/maps/place/"+location)



#@eel.expose
def shownote():
    speak("Showing notes")
    file=open("jarvis.txt","r")
    print(file.read())
    speak(file.read())



@eel.expose
def allcmd() :
    while True :
      check=takeCommand().lower()
      if 'hey jarvis' in check or 'hello jarvis' in check or 'jarvis' in check or 'okay jarvis' in check :
       wishMe()
       username() 
       while True:
        
        order=takeCommand().lower()
        if 'how are you ' in order:
              speak("I am fine , Thankyou for asking ")
              speak("How are you , Sir ?")
              
        elif 'fine' in order or 'good' in order:
              speak("it's good to know that you are fine.")
 
        elif 'who i am ' in order :
              speak('if you can talk then surely you are aa human . ')
 
        elif 'who are you' in order:
              speak('i am your virtual assistant jarvis.')
 
        elif ' what is your name ' in order :
              speak('my frineds call me jarvis .')

        elif 'search' in order or 'what is' in order or 'what' in order or 'who is' in order or 'who' in order or'when' in order :
              GEMINI_SEARCH(order)
        
        elif 'on google' in order and 'search'  in order :
              order=order.replace("on google search for" , " ")
              search_querry(order)

        elif 'open google' in order:
              speak("here you go to google sir\n")
              webbrowser.open("google.com")

        elif 'open youtube' in order:
              speak("here you go to youtube sir")
              webbrowser.open("youtube.com")

        

        elif 'open amazon' in order:
              speak("here you go to amazon sir. happy shopping")
              webbrowser.open("amazon.in")
 
        elif 'open stackoverflow' in order:
              speak("here you go to stack overflow. happy coding")
              webbrowser.open("stackoverflow.com")
        
        elif 'open myntra' in order :
            speak("Here you go to myntra sir. Happing shopping \n")
            webbrowser.open("myntra,com")

        elif ' cpu status' in order :
            cpu()

        elif 'bmi' in order :
             bmi()
        elif'take a screenshot' in order or 'screenshot this' in order:
            screenshot()

        elif 'exit' in order or 'quit' in order or 'thank you ' in order : 
            speak("Thankyou for sir. have a good day")
            sys.exit()

        elif 'shutdown' in order or 'turn off' in order :
            shutdown()
        elif 'restart' in order :
            subprocess.call(['shudown','/r'])

        elif 'hibernate' in order :
            speak('Hibernating....')
            subprocess.call(['shutdown','/h'])

        elif 'log off 'in order :
            speak(' make sure all of your applications are closed before signing out sir !')
            time.sleep(5)
            subprocess.call(['shutdown','/i'])

        elif "where is" in order:
            locate()
 
        elif "write a note" in order or 'create note' in order or 'add a note' in order :  
            note()
        elif 'show note' in order or 'show notes' in order or 'my notes' in order :
            shownote()

        elif 'joke' in order:
            speak(pyjokes.get_joke(Language="e",category="neutral"))

        elif 'the time' in order:           
            strTime=datetime.now().strftime("%H:%M:%S")
            speak(f"Well, the time is {strTime}")

        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        elif 'empty recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False, show_progress = False, sound=True)
            speak("recycle bin recycled")
        elif 'camera' in order:
            cam()
        elif ' ' in order:
            GEMINI_SEARCH(order)
       else:
         continue
      else:
        continue