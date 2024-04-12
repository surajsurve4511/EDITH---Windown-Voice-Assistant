import os
import eel


from engine.features import *
from engine.command import *
from engine.core import *

def start():
    
    eel.init("www")

    playAssistantSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('www/assets/index.html', mode=None, host='localhost', block=True)
    
    allcmd()

start()