import pyttsx3
enngine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engnie.setProperty('voice' , voices[1].1d)

def speak(audio)
     engine.say(audio)
     print(audio)
     enginerunAndWait()
def takeCommand():
     r=sr.Recognizer()
     with sr.Microphone() as source :
         print("Listening ......")
         r..pause_threshold=1
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
    
if __name__=='__main_'
        
    
                          