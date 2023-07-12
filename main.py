import qrcode
from tkinter import *
from tkinter import Image,PhotoImage
from PIL import Image,ImageTk
#import image
w =Tk()
w.geometry('400x500')
w.title('QRCode Generator')
w.config(background= '#5A67A5')

qr = qrcode.QRCode(
    version=3, #higer the version,bigger picture n more complex it is
    box_size= 12, #size of box where qr code is formed
    border=3,#border of qrcode
)
entry=Entry(w,font=("times",20,'bold'))
entry.pack()

def qrc():
    data = entry.get()
    qr.add_data(data) #qr is made
    qr.make(fit=True)
    img=qr.make_image(fill= 'black',back_color='white')
    img.save('img.png') #qr completion complete
    img1 = ImageTk.PhotoImage(file='img.png') #qr is converted into python img
    l=Label(w,width=400,height=400,image=img1)# img is assigned to a label
    l.pack()
b=Button(text='Generate QR',command=qrc)
b.pack()
w.mainloop()
