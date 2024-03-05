from GoogleNews import GoogleNews 

def news():
    news =GooglNews(period='1d')
    news.search("India")
    result = news.result()
    #print(result)
    data = pd.DataFrame.from_dict(result)
    data = data.drop(column=["img"])
    print(data.head())
    for i in result:
        print(i["title"])
news()


elif 'news' in order:
    news()

elif 'password' in order:
    password()



import pandas as pd
import string 

def password():
    char = string.ascii_letters + string.digits
    return".join(random.choice(char) for x is in range(0,15))
print(random())


from tkinter import*
import calendar

def show():
    root= Tk()
    root,config(background='grey)
    root.title('Calender')
    root.geometry('500x660')
    year = int (year_field.get())
    context = calender.calender. (year)
    cal_year = Label(root, text=context, font="times 10 bold")
    cal_year.grid(row=5, column=1, padax=10)
    root.mainloop  

 

if__name__=="__ main__":
   new = Tk()
   new.config(background='grey')
   new.title('calender')
   new.geometry('150x150')

   cal = Label(new, text="Calendar", bg='grey' , font=("times",25,"bold"))
   cal.grid(row=1, column=1)
   year =Label(new, text="Enter Year; ", bg='dark grey') 
   year.grid(row=2, column=1)
   year_field = Entry(new)
   year_field,grid(row=3, column=1)
   button =Button(new, text='show Calender', fg='black', bg='grey', coomand show)
   button.grid(row=4, column=1)
   new.mainloop()









































































