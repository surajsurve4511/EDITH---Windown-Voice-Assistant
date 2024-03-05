elif 'switch window' in order :
     pyautogui.keyDown('alt')
     pyautogui.press('tab')
     time.sleep(1)
     pyautogui.keyUp('alt')
elif 'take a screenshot' in order or 'screenshot' in order :
     speak('Sir, please tell me the name for this file.')
     name = takeCommand().lower()
     speak("please hold the screen for a while')
     time.sleep(3)
     img = pyautogui.screenshot()
     img.save(f"(name).png")
     speak("screenshot captured !")
elif 'cpu status' in order :
     cpu()
elif 'empty recycle bin' in order :
     winshell.recycle_bin().empty(confirm=False, show_progress = False , sound = True)
     speak("recycle bin cleaed")
elif 'camera' in order :
     cam()
elif 'ip' in order :
     host = socket.gethostname()
     ip = socket.gethostname(host)
     speak("your IP address is" + ip )
elif 'bmi' in order :
     speak("Please tell your height in centimetres")
     height =takeCommand()
     speak("Please tell your weight in kilograms")
     weight = takeCommand()
     height = height/100
     BMI = weight/(height*height)
     speak("Your body mass index is " + BMI)
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
          



          
          
