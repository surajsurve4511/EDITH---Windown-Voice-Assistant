def opencommand(query):
  query = query.replace(ASSISTANT_NAME,"")
  query = query.replace("open"."")

  if query!="":
    speak("Opening"+query)
    os.system('start'+query)
  else:
    speak("not found")

def allCommands()
  query = takeCommand()
  print(query)
  if "open" in  query:
    openCommand(query)
  else :
    print("not run")
    
