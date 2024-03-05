elif 'empty recycle bin' in order:
     winshell.recycle_bin().empty(confirm=False, show_progress = False, sound=True)
     speak("recycle bin recycled")
