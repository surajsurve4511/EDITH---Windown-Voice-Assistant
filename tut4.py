elif 'shutdown' is order or 'turn off' in order :
     speak('Hold on a second sir! Your system is on itsa way to shutdown')
     speak('MAke sure all of your applications are closed')
     time.sleep(5)
     subprocess.call(['shudown','/s'])
elif 'restart' in order :
     subprocess.call(['shudown','/r'])
elif 'hibernate' in order :
     speak('Hibernating....')
     subprocess.call(['shutdown','/h'])
elif 'log off 'in order :
     speak(' make sure all of your applications are closed before signing out sir !')
     time.sleep(5)
     sunprocess.call(['shutdown','/i'])
