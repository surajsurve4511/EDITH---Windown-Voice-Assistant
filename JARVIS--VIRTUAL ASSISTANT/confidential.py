import pyttsx3
import speech_recognition as sr
import webbrowser
import webbrowser
import datetime
import time
import os
import psutil
import wikipedia


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)



def username():
    speak("What shoudi call you")
    uname=takeCommand()
    speak("Welcome Mister"+uname) 
    speak("How can i help you ?")

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

        elif 'search' in order :
              order=order.replace("search for", " ")
              search_querry(order)

        elif 'search on wikipedia' in order:
              speak('Searching...')
              order=order.replace("wikipedia","")
              results=wikipedia.summary(order,sentence=2)
              speak("According to wikipedia")
              speak(results)                  

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
