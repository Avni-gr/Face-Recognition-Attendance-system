from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from Student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

 #first image
        img=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\f lable 1.jpg")
        img=img.resize((1550,180),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=180)

  #BG image and label
        img3=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\0c32e377223425.5c8132868e9be.jpg")
        img3=img3.resize((1550,750),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=180,width=1550,height=750)

        title_lbl=Label(bg_img,bg="white")
        title_lbl.place(x=0,y=-5,width=1550,height=8)

        #----------time-----
        def time():
            string = strftime("%H:%M:%S" )
            lbl.config(text = string)
            lbl.after(1000, time)
            now = datetime.now()

        lbl = Label(f_lbl,font=("Times new roman",20,"bold"),bg="White",fg="#646FD4") 
        lbl.place(x=1400,y=0,width=110,height=50)  
        time()

   #Student Button    
        img4=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Student details.png")
        img4=img4.resize((250,280),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=50,width=250,height=200) 

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Times new roman",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=250,y=250,width=250,height=40)     

    #Detect Face Button  
        img5=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Face detect.png")
        img5=img5.resize((250,280),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data,)
        b1.place(x=530,y=50,width=250,height=200) 

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Open Sans",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=530,y=250,width=250,height=40)

    #Attendance Button  
        img6=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Attedance.png")
        img6=img6.resize((240,250),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=810,y=50,width=250,height=200) 

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Open Sans",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=810,y=250,width=250,height=40) 

    #Help Button  
        img7=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Help.png")
        img7=img7.resize((230,260),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Help)
        b1.place(x=1090,y=50,width=250,height=200) 

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.Help,font=("Open Sans",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=1090,y=250,width=250,height=40)

    #Train Button  
        img8=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Train data.png")
        img8=img8.resize((260,240),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.Train_data,cursor="hand2")
        b1.place(x=250,y=330,width=250,height=200) 

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.Train_data,font=("Open Sans",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=250,y=530,width=250,height=40)

    #Photos Button  
        img9=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\photos.png")
        img9=img9.resize((250,250),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=530,y=330,width=250,height=200) 

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Open Sans",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=530,y=530,width=250,height=40)

    #Developer Button  
        img10=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\developer.png")
        img10=img10.resize((250,250),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Developer)
        b1.place(x=810,y=330,width=250,height=200) 

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer,font=("Open Sans",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=810,y=530,width=250,height=40)

    #Exit Button  
        img11=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Exit.png")
        img10=img11.resize((300,290),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1090,y=330,width=250,height=200) 

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Open Sans",20,"bold"),bg="#646FD4",fg="White")
        b1_1.place(x=1090,y=530,width=250,height=40) 

    def open_img(self):
                os.startfile("Img_data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","are you sure to exit ?",parent=self.root) 
        if self.iExit > 0:
            self.root.destroy()
        else:
            return            

#Function Button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def Train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)   

    def Developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)   

    def Help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)           


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root) 
    root.mainloop()