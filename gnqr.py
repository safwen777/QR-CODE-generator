#FIRST OF ALL YOU HAVE TO INSTALL  TKINTER AND QR CODE AND OPENCV LIBRARIES
from tkinter import  *
import qrcode
#YOU NEED TO INSTALL OPENCV-PYTHON FIRST TO USE CV2
import cv2
window=Tk()
window.geometry("400x250")
window.title("QR CODE GENRATOR")
nom=Label(window,text="GENERATE QR CODE",fg="white",bg="blue",font=("Stencil",21))
nom.pack(fill=X)
en=Entry(window,justify=LEFT,font=("Stencil",20),bd=2,relief=RIDGE,width=20)
en.place(x=28,y=50)
def gener(enent=NONE):
    image=qrcode.make(en.get())
    image.save("qr.jpg")
    image=cv2.imread("qr.jpg")
    cv2.imshow("fen",image)
    cv2.waitKey(1000)
b1=Button(window,text="GENERATE ",font=('Arial',15),bg='white',bd=0,relief=GROOVE,width=30,cursor='hand1',command=gener)
b1.place(x=20,y=100)
b2=Button(window,text="QUIT ",font=('Arial',15),bg='red',bd=0,relief=GROOVE,width=30,cursor='hand1',command=window.quit)
b2.place(x=20,y=130)
window.mainloop()
