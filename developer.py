from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

        title_lbl=Label(self.root,text="Developer",font=("Open Sans",20,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=4,width=1550,height=60)

        img3=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\blur blue.jfif")
        img3=img3.resize((1550,750),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1550,height=750)

        main_frame=Frame(bg_img,bd=2,bg="#DCDCDC")
        main_frame.place(x=250,y=20,width=1000,height=700)

        img4=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Avni Gour.jpg")
        img4=img4.resize((1000,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(main_frame,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1000,height=700)


if __name__ =="__main__":
    root=Tk()
    obj=Developer(root) 
    root.mainloop()