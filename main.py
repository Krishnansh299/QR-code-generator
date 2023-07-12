from tkinter import *
import speedtest

def speed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    up=str(round(sp.download()/(10**6),3))+'Mbps'
    down= str(round(sp.download() / (10 ** 6), 3)) + 'Mbps'
    b1.config(text=down)
    b3.config(text=up)
w=Tk()
w.title('speed test')
w.geometry('600x400')
l=Label(w,text="Internet Speed Test",font=(30))
l.pack()
b=Button(w,text='Download Speed',borderwidth=0,font=(30))
b.place(x=230,y=50)
b1=Button(w,text='00',borderwidth=0,font=(30))
b1.place(x=280,y=100)
b2=Button(w,text='Upload Speed',borderwidth=0,font=(30))
b2.place(x=230,y=150)
b3=Button(w,text='00',borderwidth=0,font=(30))
b3.place(x=280,y=200)
b4=Button(w,text='Check Speed',font=(30),command=speed)
b4.place(x=230,y=250)


w.mainloop()