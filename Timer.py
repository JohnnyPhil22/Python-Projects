import time, winsound
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry('300x250')
root.title('Timer')

hr,min,sec=StringVar(),StringVar(),StringVar()

hr.set('00')
min.set('00')
sec.set('00')

hrLabel=Label(root,text='Hours',font=('Arial', 14, ''),justify=CENTER)
hrLabel.place(x=55,y=55)
hrEntry=Entry(root,width=3,font=('Arial', 18, ''),textvariable=hr,justify=CENTER)
hrEntry.place(x=62,y=85)

minLabel=Label(root,text='Minutes',font=('Arial', 14, ''),justify=CENTER)
minLabel.place(x=110,y=55)
minEntry=Entry(root,width=3,font=('Arial', 18, ''),textvariable=min,justify=CENTER)
minEntry.place(x=126,y=85)

secLabel=Label(root,text='Seconds',font=('Arial', 14, ''),justify=CENTER)
secLabel.place(x=180,y=55)
secEntry=Entry(root,width=3,font=('Arial', 18, ''),textvariable=sec,justify=CENTER)
secEntry.place(x=200,y=85)

def submit():
    try:
        temp=int(hr.get())*3600+int(min.get())*60+int(sec.get())
    except:
        print('Please input the right value')
    while temp>-1:
        mins,secs=divmod(temp, 60)

        hours=0
        if mins>60:
            hours,mins=divmod(mins, 60)
        hr.set('{0:2d}'.format(hours))
        min.set('{0:2d}'.format(mins))
        sec.set('{0:2d}'.format(secs))

        root.update()
        if temp!=0:
            winsound.Beep(1000, 500)
        time.sleep(1)

        if temp==0:
            winsound.Beep(2000, 500)
            messagebox.showinfo("Timer", "Time's up",)

        temp-=1


btn=Button(root,text='Set Timer',bd=5,command=submit)
btn.place(x=113,y=120)

root.mainloop()