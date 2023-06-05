from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Userregister:
    
    # **********function declaration******
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error","All fields are required!")

        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please agree to our terms and conditions!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aayush@123",database="face_recognizer_db")
            my_cursor= conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist. Please try another email.")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registeration Successfuly")

    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1090+0+0")


        # ************text variables********
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        img4 = Image.open(r"college_images\img15.jpeg")
        img4 = img4.resize((1920,1090),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0,y=0,width=1920,height=1090)



        # *****frame******
        frame = Frame(self.root, bg="white")
        frame.place(x = 600, y = 180,width=800, height= 650)

        register_lbl = Label(frame, text= "Register Here", font= ("times new roman",30,"bold") , fg="darkgreen" ,bg = "white")
        register_lbl.place(x= 80, y = 60)

        # ************row 1******
        fname = Label(frame, text = "First Name", font= ("times new roman",20,"bold") ,bg = "white")
        fname.place(x= 50 , y = 120)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font= ("times new roman",20,"bold") )
        fname_entry.place(x = 50 , y =150, width = 300)

        lname = Label(frame, text = "Last Name", font= ("times new roman",20,"bold") ,bg = "white")
        lname.place(x= 450 , y = 120)

        self.txt_lname = ttk.Entry(frame,textvariable= self.var_lname,font= ("times new roman",20) )
        self.txt_lname.place(x = 450 , y =150, width = 300)

        # *********row 2*********
        contact = Label(frame, text = "Contact No.", font= ("times new roman",20,"bold") ,bg = "white")
        contact.place(x= 50 , y = 200)

        self.txt_contact = ttk.Entry(frame,textvariable= self.var_contact,font= ("times new roman",20) )
        self.txt_contact.place(x = 50 , y =230, width = 300)

        email = Label(frame, text = "Email", font= ("times new roman",20,"bold") ,bg = "white")
        email.place(x= 450 , y = 200)

        self.txt_email = ttk.Entry(frame,textvariable= self.var_email,font= ("times new roman",20) )
        self.txt_email.place(x = 450 , y =230, width = 300)

        # **********row 3*******
        security_Q = Label(frame, text = "Select Security Question", font= ("times new roman",20,"bold") ,bg = "white")
        security_Q.place(x= 50 , y = 280)

        self.combo_security_Q = ttk.Combobox(frame, textvariable= self.var_securityQ , font= ("times new roman",15,"bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Favourite Fruit", "Your Bestfriend name")
        self.combo_security_Q.place(x=50, y = 320, width=300)
        self.combo_security_Q.current(0)



        security_A = Label(frame, text = "Security Answer", font= ("times new roman",20,"bold") ,bg = "white")
        security_A.place(x= 450 , y = 280)

        self.txt_security = ttk.Entry(frame, textvariable= self.var_securityA ,font= ("times new roman",20) )
        self.txt_security.place(x = 450 , y =320, width = 300)

        # *********row 4 ******
        pswd = Label(frame, text = "Password", font= ("times new roman",20,"bold") ,bg = "white")
        pswd.place(x= 50 , y = 370)

        self.txt_pswd = ttk.Entry(frame,textvariable= self.var_pass ,font= ("times new roman",20) )
        self.txt_pswd.place(x = 50 , y =400, width = 300)

        confirm_pswd = Label(frame, text = "Confirm Password", font= ("times new roman",20,"bold") ,bg = "white")
        confirm_pswd.place(x= 450 , y = 370)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable= self.var_confpass,font= ("times new roman",20) )
        self.txt_confirm_pswd.place(x = 450 , y =400, width = 300)

        # ****checkButton*********
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable= self.var_check, text = "I Agree the Terms & Conditions",font= ("times new roman",15,"bold"),onvalue=1,offvalue=0, bg="white")
        checkbtn.place(x=50,y = 480)

        # *******buttons*******
        img = Image.open(r"college_images\img30.jpeg")
        img = img.resize((300,80),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image= self.photoimage,command= self.register_data,cursor="hand2", borderwidth=0)
        b1.place(x = 10, y= 520, width = 300)

        img1 = Image.open(r"college_images\img33.jpeg")
        img1 = img1.resize((300,80),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,image= self.photoimage1,cursor="hand2", borderwidth=0)
        b1.place(x = 410, y= 520, width = 300)

        
             

if __name__ == "__main__":
    root = Tk()
    app = Userregister(root)
    root.mainloop()