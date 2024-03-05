import pyttsx3
import speech_recognition


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def speak(audio) :
     engine.say(audio)
     print(audio)
     enginerunAndWait()
     
def takeCommand():
     r=sr.Recognizer()
     with sr.Microphone() as source :
         print("Listening ......")
         r.pause_threshold=1
         audio=r.listen(source, timeout=1,phrase_time_limit=10)
         try:
             print("Recognizing....")
             query=r.recognize_google(audio,language='en-in')
             print(f"User said {query}\n")
         except Exception as e :    
             speak(f"Unableto recognize yoour voice......")
             return"None"
         return query 
def username():
    speak("What shoudi call yoou sir")
    uname=takeCommand()
    speak("Welcome Mister"+uname) 
    speak("How cani help you Sir ?")

if __name__=='__main_' :
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

