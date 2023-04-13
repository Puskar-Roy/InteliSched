from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import *
import subprocess

w=Tk()


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

def new_win():
    q=Tk()
    q.title('Main window')
    q.geometry('427x250')
    l1=Label(q,text='ADD TEXT HERE ',fg='grey',bg=None)
    l=('Calibri (Body)',24,'bold')
    l1.config(font=l)
    l1.place(x=80,y=100)
    q.mainloop()



def bar():

    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    w.destroy()
    subprocess.run(["python3","d_login_page.py"])
    # new_win()
        
    
progress.place(x=-10,y=235)

a='#249794'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=15,height=1,text='Launch',command=bar,border=0,fg="white",bg='black')
b1.place(x=250,y=180)

l1=Label(w,text='Intelli',fg='white',bg=a)
lst1=('Calibri (Body)',30,'bold')
l1.config(font=lst1)
l1.place(x=155,y=80)

l2=Label(w,text='Sched',fg='white',bg=a)
lst2=('Calibri (Body)',30)
l2.config(font=lst2)
l2.place(x=260,y=82)



img1 = PhotoImage(file="logo1 (1).png")
label = Label(w, image=img1,text="",height=50,width=55)
label.place(x=80,y=77)

w.mainloop()


