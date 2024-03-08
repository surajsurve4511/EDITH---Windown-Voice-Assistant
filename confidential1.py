import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import time
import os
import random
import pyjokes
import time
import pyautogui
import psutil
import winshell
import socket
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
   camera import*
import socket
import imdb   
from GoogleNews import GoogleNews
import pandas as pd
import string

def password():
    char = string.ascii_letters + string.digits
    return".join(random.choice(char) for x is in range(0,15))
print(random())

def username():
    speak("What shoudi call yoou sir")
    uname=takeCommand()
    speak("Welcome Mister"+uname) 
    speak("How cani help you Sir ?") 

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery=str(psutil.sensors_battery())
    speak("Battery is at"+battery)    

def cam() :
    import tkinter
    from tkinter import messagebox
    import PIL.Image, PIL.ImageTk
    import time

    class App:
        def _init_(self,window, window_title, video_source=0)
            self.window = window
            self.window.title = (window_title)
            self.video_source = video_source

            self.vid = HyVideoCapture(self.video_source)
            self.canvas = tkinter.Canvas(window, height=self.vid.height, width=self,vid,width)
            self.canvas.pack()

            btn_frame = tkinter.Frame(window, background="Black")
            btn_frame.place(x=0,y=0)

            self.btn_snapshot = tkinter.Button(btn_frame,text="Snapshot", width=20, bg="black", fg="white")
            self.btn_snapshot.pack(side="left",padx=10,pady=10)

            self delay = 15
            self.update()


            self.window.mainloop()

         def snapshot(self):
             ret, frame = self.vid.get_frame()
             if ret:
                 cv2.imwrite ("My Capture "+ time.strftime("%d-%m-%Y-%H-%m-%s")+", jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
                 messagebox.shoeinfo("Notification","Image Saved")
        
         def update(self):
             ret, frame =self.vid.get_frame()

             if ret:
                 self.photo = PIL.Image.Tk.PhotoImage(image=PIL.image.fromarray((frame))
                 self.canvas.create_image(0,0, iamge=self,photo, anchor=tkinter.NW)

                 self.window.after(self.delay,self.update)






     class MyVideoCapture:
         def _init_(self, video_source=0)
             self.vid = cv2.VideoCapture(video_source)
             if not self.vid.isOpened():
                raiseValueError("Unable to open video Source", video_source)

             self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
             self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

         def get_frame(self):
             if self.vid.isOpened() :
                ret, frame = self.vid.read()
                if ret:
                    return(ret, cv2.cvtColor(frame, cv2.COLOR_BGR@RGB))
                else:
                    return(ret, None)
             else: 
                 return(ret,None)
         def_del_(self) :
             if self.vid.isOpened():
                  self.vid.release()       

      App(tkinter.Tk(),"Camera")
  cam()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am your virtual assistant Jarvis.")

def speak(audio) :
     engine.say(audio)
     print(audio)
     engine.runAndWait()
     
def takeCommand():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listning....!")
       audio = r.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
       print("You said : " + r.recognize_google(audio))
       query=r.recognize_google(audio)
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return query

def search_querry(query) :
    search_url= f'https://www.google.com/search?q={query}'
    webbrowser.open_new_tab(search_url)

def movie ():
     moviesdb = imdb.IMDb()
     speak("Please tell me the movie name sir")
     text = takeCommand()
     movies = moviesdb.search_movie(text)
     speak("Searching for " + text )
     if len(movies==0):
         speak("No results found")
     else:
         speak("I found these :")
         for movie in movies :
              title = movie["title"]
              year = movie["year"]
              speak(f'{title}-{year}')
              info = movie.getID()
              movie = moviesdb.get_movie(info)
              rating = movie["rating"]
              plot = movie['plot outline']
              if year<int(datetime.datetime.now().strftime("%Y")):
                   speak(f'{title} was released in {year} has IMDB ratings of {rating} . The plot summary of movie is {plot} ')
                   break
              else:
                   speak(f'{title} will be released in {year} has IMDB ratings oof {rating} . The plot summary of movie is {plot} ')
                   break



if __name__==  '__main__' :
    wishMe()
    username()
    while True :
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
 
        elif 'open notepad' in order :
              npath="C:\Windows"
              os.startfile(npath)
 
        elif 'search' in order :
              order=order.replace("search for", " ")
              search_querry(order)
        
        elif 'play music' in order or 'play songs' in order:
              music_dir="D:\\Music"
              songs=os.listdir(music_dir)
              rd=random.choice(songs)
              os.startfile(os.path.join(music_dir ,rd))

        elif 'search on wikipedia' in order:
              speak('Searching...')
              order=order.replace("wikipedia","")
              results=wikipedia.summary(order,sentence=2)
              speak("According to wikipedia")
              speak(results)

        elif 'open google' in order:
              speak("here you go to google sir\n")
              webbrowser.open("nyntra.com")

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
        elif "where is" in order:
            order=order.replace("Where is" ,"")
            location+order
            speak("Locating.....")
            speak(Location)
            webbrowser.open("https://www.google.co.in/maps/place/"+Location+"")

        elif "write a note" in order:
            speak("What should i write , sir?")
            note=takeCommand()
            file=open('jarvis,txt','w')
            speak("Sir, Should I include date and time as well?")
            sn=takeCommand()
            if 'yes' or 'sure'or 'yeah' in sn:
              strTime=datetime.now().strftime("%H:%M:%S")
              file.write (strTime)
              file.write(note)
              speak("Done Sir!")
            else:
                file.write(note)
                speak("Done Sir!")

        elif 'shown note' in order:
            speak("Showing notes")
            file=open("jarvis.txt","r")
            print(file.read())
            speak(file.read(6))

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

        elif 'take a screenshot' in order or 'screeenshot this' in order:
            speak('Sir, please tell me the name for this file.')
            name=takeCommand().lower()
            speak("please hold the screen")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{nmae}.png")
            speak("screenshot captured sir!")
        elif 'cpu status' in order :
            cpu()   

        elif 'empty recycle bin' in order:
             winshell.recycle_bin().empty(confirm=False, show_progress = False, sound=True)
             speak("recycle bin recycled")
        elif 'camera' in order:
             cam()

        elif 'exist' in order or 'quit' in order: 
             speak("Thankyou fo using me sir. have a good day")
             sys.exit() 

        elif 'ip' in order :
             host = socket.gethostname()
             ip = socket.gethostname(host)
             speak("your IP address is" + ip )
        elif 'bmi' in order :
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
                  speak("Enter valid details)
        elif 'movie' in order :
                  movie()          

        elif 'news' in order:
                  news()

        elif 'password' in order:
                  password()
         

