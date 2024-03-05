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


          
          
