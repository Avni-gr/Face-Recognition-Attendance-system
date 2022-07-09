from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

        title_lbl=Label(self.root,text="Train Data Set",font=("Open Sans",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=4,width=1550,height=60)

        img3=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\blur blue.jfif")
        img3=img3.resize((1550,750),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1550,height=750)

        #train data set Button    
        img4=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\face ai.jpg")
        img4=img4.resize((400,400),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.train_classifier,cursor="hand2")
        b1.place(x=560,y=100,width=420,height=420) 

        b1_1=Button(bg_img,text="Click here to Train",cursor="hand2",command=self.train_classifier,font=("Times new roman",20,"bold"),bg="blue",fg="White")
        b1_1.place(x=560,y=520,width=420,height=40)

        # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("Img_data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[] #images nd id should be same
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert in gray scale 
            imageNp = np.array(img,'uint8') #for convert into grid with the help of numpy #uint is datatype
            id=int(os.path.split(image)[1].split('.')[1])  #in any particular file path there is file path and then file name so file path is 0 and file name is 1 but there name is 1.1 so we are spliting becoz first 1 is user id and seconf 1 is image count 

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13 #after enter window should be close
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml") #train data will store in this file

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)







# main class object
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        
