from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = [] # global variable for store xl list
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()

        #first image
        img=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\Attendance system.jpg")
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

        main_frame=Frame(bg_img,bd=2,bg="#DCDCDC")
        main_frame.place(x=0,y=3,width=1550,height=602)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="#DCDCDC",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=20,y=10,width=730,height=580)

        img4=Image.open(r"C:\Users\Dell Guna\OneDrive\Desktop\Face recognition attendance\Project Images\happy-pupils-studying-classroom-isolated-flat-illustration-cartoon-children-characters-sitting-tables-school-lesson_74855-10790.webp")
        img4=img4.resize((720,195),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(left_frame,image=self.photoimg4)
        f_lbl.place(x=2,y=0,width=720,height=190)

        leftin_frame = LabelFrame(left_frame,bd=2,bg="#DCDCDC",relief=RIDGE,font=("verdana",12,"bold"),fg="navyblue")
        leftin_frame.place(x=20,y=190,width=700,height=220)
        


        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(leftin_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="#DCDCDC")
        studentId_label.grid(row=0,column=0,padx=15,pady=15,sticky=W)

        studentId_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_id,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=15,pady=15,sticky=W)

        #Student Roll
        student_roll_label = Label(leftin_frame,text="Roll.No:",font=("verdana",12,"bold"),fg="navyblue",bg="#DCDCDC")
        student_roll_label.grid(row=0,column=2,padx=15,pady=15,sticky=W)

        student_roll_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_roll,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=10,pady=15,sticky=W)

        #Studnet Name
        student_name_label = Label(leftin_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="#DCDCDC")
        student_name_label.grid(row=1,column=0,padx=15,pady=15,sticky=W)


        student_name_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_name,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=15,pady=15,sticky=W)

        #Department
        dep_label = Label(leftin_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="#DCDCDC")
        dep_label.grid(row=1,column=2,padx=15,pady=15,sticky=W)

        dep_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_dep,font=("verdana",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=15,sticky=W)

        #time
        time_label = Label(leftin_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="#DCDCDC")
        time_label.grid(row=2,column=0,padx=15,pady=15,sticky=W)

        time_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_time,font=("verdana",12,"bold"))
        time_entry.grid(row=2,column=1,padx=15,pady=15,sticky=W)

        #Date 
        date_label = Label(leftin_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="#DCDCDC")
        date_label.grid(row=2,column=2,padx=15,pady=15,sticky=W)

        date_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_date,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=15,sticky=W)

        #Attendance
        student_attend_label = Label(leftin_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="#DCDCDC")
        student_attend_label.grid(row=3,column=0,padx=15,pady=15,sticky=W)

        attend_combo=ttk.Combobox(leftin_frame,width=13,textvariable=self.var_attendance,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3,column=1,padx=15,pady=15,sticky=W)

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="#DCDCDC",relief=RIDGE)
        btn_frame.place(x=20,y=420,width=700,height=60)

        #Improt button
        save_btn=Button(btn_frame,text="Import CSV",width=12,command=self.importCsv,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=15,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,text="Export CSV",width=12,command=self.exportCsv,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=15,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=15,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=12,command=self.reset_data,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=15,pady=10,sticky=W)

        # right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="#DCDCDC",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=780,y=10,width=730,height=580)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="#DCDCDC",relief=RIDGE)
        table_frame.place(x=15,y=0,width=700,height=500)
        
        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Std-ID")
        self.attendanceReport.heading("Roll_No",text="Roll.No")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attendance",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Department",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attendance",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)
        

        # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        mydata = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
                self.attendanceReport.insert("",END,values=i)
                print(i)
        

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                    mydata.append(i)
                    self.fetchData(mydata)

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #=============Cursur Function for CSV========================

    def get_cursor(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        rows = content["values"]

        self.var_id.set(rows[0]),
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_time.set(rows[4]),
        self.var_date.set(rows[5]),
        self.var_attendance.set(rows[6]) 

    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Status")   




if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root) 
    root.mainloop()        

