from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

        title_lbl=Label(self.root,text="Help Desk",font=("Open Sans",20,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=4,width=1550,height=60)

        img3=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\blur blue.jfif")
        img3=img3.resize((1550,750),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1550,height=750)

        main_frame=Frame(bg_img,bd=2,bg="#DCDCDC")
        main_frame.place(x=250,y=20,width=1000,height=700)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Linkedin button 1
        std_img_btn=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\linkedin.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(main_frame,command=self.Linkedin,image=self.std_img1,cursor="hand2")
        std_b1.place(x=50,y=200,width=180,height=180)

        std_b1_1 = Button(main_frame,command=self.Linkedin,text="Linkedin",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=50,y=380,width=180,height=45)

        # Github Face  button 2
        det_img_btn=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\github.png")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(main_frame,command=self.Github,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=280,y=200,width=180,height=180)

        det_b1_1 = Button(main_frame,command=self.Github,text="Github",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=280,y=380,width=180,height=45)

         # Instagram System  button 3
        att_img_btn=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Instagram.jfif")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(main_frame,command=self.Instagram,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=510,y=200,width=180,height=180)

        att_b1_1 = Button(main_frame,command=self.Instagram,text="Instagram",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=510,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\email.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(main_frame,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=740,y=200,width=180,height=180)

        hlp_b1_1 = Button(main_frame,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=740,y=380,width=180,height=45)


        # create function for button 
    
    
    def Linkedin(self):
         self.new = 1
         self.url = "https://www.linkedin.com/in/avni-gour-aa2375201/"
         webbrowser.open(self.url,new=self.new)
    
    def Github(self):
        self.new = 1
        self.url = "https://github.com/Avni-gr"
        webbrowser.open(self.url,new=self.new)
    
    def Instagram(self):
        self.new = 1
        self.url = "https://instagram.com/tiya.aa_?igshid=YmMyMTA2M2Y="
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://mail.google.com/mail/u/0/#inbox?compose=CllgCJfmrDVKPKcFfvKCKPVxZCmTGHKkFKlVTckdzCSCWpSbxzXRShxkvDdNCzJTlMkSzHMvJwg"
        webbrowser.open(self.url,new=self.new)

if __name__ =="__main__":
    root=Tk()
    obj=Help(root) 
    root.mainloop()        