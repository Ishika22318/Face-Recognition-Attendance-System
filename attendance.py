from tkinter import *
from tkinter import ttk, Frame
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.title("face Recognition System")

        # **********variables********
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # FIRST image
        img1 = Image.open(r"college_images\img19.jpeg")
        img1 = img1.resize((960,300),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0,y=0,width=960,height=300)

        # second image
        img2 = Image.open(r"college_images\img20.jpeg")
        img2 = img2.resize((960,300),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=960,y=0,width=960,height=300)

        #bg - image
        # third image
        img3 = Image.open(r"college_images\img15.jpeg")
        img3 = img3.resize((1920,800),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0,y=280,width=1920,height=800)

        title_lbl = Label(bg_img,text="Attendance MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1920,height=60)

        main_frame=Frame(bg_img,bd=2,bg="white",)
        main_frame.place(x=0,y=85,width=1920,height=610)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance details",font=("times new roman",20,"bold"))
        Left_frame.place(x=15,y=5,width=900,height=550)

        left_inner_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white",)
        left_inner_frame.place(x=5,y=10,width=865,height=530)

        # attendance id
        attendanceId_label = Label(left_inner_frame,text="Attendance Id:",font=("times new roman",15,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=20,pady=15,sticky=W)

        attendanceId_entry=ttk.Entry(left_inner_frame,width=30,textvariable=self.var_atten_id,font=("times new roman",15,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=15,sticky=W)

        # Roll no
        roll_no_label = Label(left_inner_frame,text="Roll No.:",font=("times new roman",15,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(left_inner_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",15,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Name
        name_label = Label(left_inner_frame,text="Student Name:",font=("times new roman",15,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inner_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",15,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        dep_label = Label(left_inner_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=5,sticky=W)

        dep_combo=ttk.Combobox(left_inner_frame,textvariable=self.var_atten_dep,font=("times new roman",15,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Electrical","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Time
        time_label = Label(left_inner_frame,text="Time:",font=("times new roman",15,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inner_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",15,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date
        date_label = Label(left_inner_frame,text="Date:",font=("times new roman",15,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inner_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",15,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # attendance status
        attendanceStatus_label = Label(left_inner_frame,text="Attendance Status:",font=("times new roman",15,"bold"),bg="white")
        attendanceStatus_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        attendanceStatus_combo=ttk.Combobox(left_inner_frame,textvariable=self.var_atten_attendance,font=("times new roman",15,"bold"),state="readonly",width=18)
        attendanceStatus_combo["values"]=("Status","Present","Absent")
        attendanceStatus_combo.current(0)
        attendanceStatus_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # buttons frame
        btn_frame = Frame(left_inner_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=30,y=340,width=820,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv ,width=17,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv , width=17,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        # ********Right label frame*********
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance",font=("times new roman",20,"bold"))
        Right_frame.place(x=930,y=5,width=960,height=550)

        Table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=5,width=935,height=530)

        # Scroll bar table
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.attendanceReportTable = ttk.Treeview(Table_frame, columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendance ID")
        self.attendanceReportTable.heading("roll",text="Roll no")
        self.attendanceReportTable.heading("name",text="Name")
        self.attendanceReportTable.heading("department",text="Department")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendance",text="Attendance Status")

        self.attendanceReportTable["show"]="headings"

        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)

        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        # =========================== FETCH DATA =============================

    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)

        # =========================== Import CSV =============================

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")) ,parent=self.root )
        # print(mydata)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            # print(csvread)
            for i in csvread:
                # print(i)
                mydata.append(i)
            # print(mydata)
            self.fetchData(mydata)
            # print(mydata)    

        # =========================== Export CSV =============================

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")) ,parent=self.root )
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    # exp_write.append(i)
                messagebox.showinfo("Data Export","Your Data is Exported to "+ os.path.basename(fln)+" successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event = ""):
        cursor_row = self.attendanceReportTable.focus()
        content = self.attendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()
