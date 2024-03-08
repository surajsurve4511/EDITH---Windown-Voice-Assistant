import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import time
import os
import random
import pyjokes
import subprocess
import time
import pyautogui
import psutil

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)



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

        elif 'shutdown' or  'turn off' in order :
            speak('Hold on a second sir! Your system is on itsa way to shutdown')
            speak('MAke sure all of your applications are closed')
            time.sleep(5)
            subprocess.call(['shudown','/s'])
        elif 'restart' in order :
            subprocess.call(['shudown','/r'])
        elif 'hibernate' in order :
            speak('Hibernating....')
            subprocess.call(['shutdown','/h'])
        elif 'log off 'in order :
            speak(' make sure all of your applications are closed before signing out sir !')
            time.sleep(5)
            sunprocess.call(['shutdown','/i'])    
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
        elif ' cpu status' in order :
            cpu()   
