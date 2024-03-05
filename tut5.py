elif 'switch window' in order:
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.keyUp('alt')

elif 'take a screenshot' in order or 'screeenshot this' in order:
    speak('Sir, please tell me the name for this file.')
    name=takeCommand().lower()
    speak("please hold the screen")
    time.sleep(3)
    img=pyautogui.screenshot()
    img.save(f"{nmae}.png")
    speak("screenshot captured sir!")
