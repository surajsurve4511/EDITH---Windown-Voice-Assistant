elif 'empty recycle bin' in order:
     winshell.recycle_bin().empty(confirm=False, show_progress = False, sound=True)
     speak("recycle bin recycled")
elif 'camera' in order:
     cam()

elif 'exist' in order or 'quit' in order: 
     speak("Thankyou fo using me sir. have a good day")
     sys.exit()
