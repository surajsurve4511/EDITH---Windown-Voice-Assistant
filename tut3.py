elif "where is" in order:
    order=order.replace("Where is" "")
    location+order
    speak("Locating.....")
    speak(Location)
    webbrowser.open("https://www.google.co.in/maps/place/"+Location+"")

elif "write a note" in order:
    speak"What should i write , sir?")
    note=takeCommand()
    file=open('jarvis,txt','w')
    speak("Sir, Should I include date and time as well?")
    sn=takeCommand()
    if 'yes' in or 'sure' in sn or 'yeah' in sn:
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
