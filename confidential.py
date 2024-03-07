import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)



def username():
    speak("What shoudi call yoou sir")
    uname=takeCommand()
    speak("Welcome Mister"+uname) 
    speak("How cani help you Sir ?")

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
        if 'search' in order :
            order=order.replace("search for", " ")
            search_querry(order)
        elif 'open amazon' in order:
            speak("here you go to amazon sir. happy shopping")
            webbrowser.open("amazon.in")
        elif 'open youtube' in order:
            speak("here you go to youtube sir")
            webbrowser.open("youtube.com")
    
