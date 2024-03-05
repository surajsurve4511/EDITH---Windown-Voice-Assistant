elif 'play music' in order or 'play songs' in order:
    music_dir="E:\\Songs\\New folder
    songs=os.listdir(music_dir)
    rd=random.choice(songs)
    os.startfile(os.path.join(music_dir ,rd))

elif 'wikipedia' in order:
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
