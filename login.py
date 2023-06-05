from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Userregister(self.new_window)

    def login(self): 
        if self.txtuser.get() == "" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required!")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success","Welcome!!!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aayush@123",database="face_recognizer_db")
            my_cursor= conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s",
                                  (self.txtuser.get(),
                                  self.txtpass.get()
                                  ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main = messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                # ishikaagarwal22318@gmail.com
                # Nish@5720
            conn.commit()
            conn.close()

    def reset_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error","Select security question",parent = self.root2)

        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter answer",parent = self.root2)
        elif self.txt_new_password.get() == "":
            messagebox.showerror("Error", "Please enter new password",parent = self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aayush@123",database="face_recognizer_db")
            my_cursor= conn.cursor()
            query = ("select * from register where email = %s and securityQ = %s and securityA = %s")
            value = (self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter correct answer",parent = self.root2)
            else:
                query = ("update register set password = %s where email = %s")
                value = (self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with new password",parent = self.root2)
                self.root2.destroy()

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error","Please enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aayush@123",database="face_recognizer_db")
            my_cursor= conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("540x650+710+270")

                l = Label(self.root2, text = "Forgot Password", font=("times new roman",30,"bold"),fg="red",bg="white")
                l.place(x = 0, y = 20 , relwidth= 1)

                security_Q = Label(self.root2, text = "Select Security Question", font= ("times new roman",20,"bold") )
                security_Q.place(x= 100 , y = 100)

                self.combo_security_Q = ttk.Combobox(self.root2 , font= ("times new roman",15,"bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Favourite Fruit", "Your Bestfriend name")
                self.combo_security_Q.place(x=100, y = 140, width=300)
                self.combo_security_Q.current(0)



                security_A = Label(self.root2, text = "Security Answer", font= ("times new roman",20,"bold") )
                security_A.place(x= 100 , y = 210)

                self.txt_security = ttk.Entry(self.root2 ,font= ("times new roman",20) )
                self.txt_security.place(x = 100 , y =250, width = 300)

                new_password = Label(self.root2, text = "New Password", font= ("times new roman",20,"bold") )
                new_password.place(x= 100 , y = 320)

                self.txt_new_password = ttk.Entry(self.root2 ,font= ("times new roman",20) )
                self.txt_new_password.place(x = 100 , y =360, width = 300)

                btn = Button(self.root2, text = "Reset",command=self.reset_password,font= ("times new roman",20,"bold"), fg = "white", bg ="green" )
                btn.place(x = 130, y = 450)
                
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1090+0+0")

        img4 = Image.open(r"college_images\img15.jpeg")
        img4 = img4.resize((1920,1090),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0,y=0,width=1920,height=1090)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=150,width=1920,height=75)

        frame = Frame(self.root, bg = "black")
        frame.place(x=710, y = 270,width = 500, height = 600)

        img1 = Image.open(r"college_images\img50.png")
        img1 = img1.resize((120,120),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg = "black",borderwidth= 0)
        lblimg1.place(x=910, y= 275, width= 100, height= 100)

        get_str = Label(frame, text = "Get Started", font = ("times new roman",30,"bold"),fg="white",bg="black")
        get_str.place(x=155,y=130)

        # label
        username_lbl = Label(frame, text= "Username", font= ("times new roman",20,"bold") , fg="red", bg="black")
        username_lbl.place(x= 80, y = 190)

        self.txtuser=ttk.Entry(frame, font = ("times new roman",20,"bold"))
        self.txtuser.place(x=50, y = 230, width= 400)

        password_lbl = Label(frame, text= "Password", font= ("times new roman",20,"bold") , fg="red", bg="black")
        password_lbl.place(x= 80, y = 290)

        self.txtpass=ttk.Entry(frame, font = ("times new roman",20,"bold"))
        self.txtpass.place(x=50, y = 330, width= 400)

        # ********icon images*****
        img2 = Image.open(r"college_images\img27.png")
        img2 = img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2,bg = "black",borderwidth= 0)
        lblimg1.place(x=760, y= 465, width= 25, height= 25)

        img3 = Image.open(r"college_images\img28.png")
        img3 = img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3,bg = "black",borderwidth= 0)
        lblimg1.place(x=760, y= 565, width= 25, height= 25)

        # ********Login button
        loginbtn = Button(frame,command = self.login, text = "Login", font = ("times new roman",30,"bold"), bd=3, relief=RIDGE, fg = "white" , bg = "red", activeforeground="white", activebackground="red")
        loginbtn.place(x=165, y=400, width=140, height=50)

        # *********Register button
        registerbtn = Button(frame, text = "New User Register",command= self.register_window,borderwidth=0, font = ("times new roman",15,"bold"), relief=RIDGE, fg = "white" , bg = "black", activeforeground="white", activebackground="black")
        registerbtn.place(x=35, y=460, width=170)

        # *****forgot password button***
        registerbtn = Button(frame,command= self.forgot_password_window, text = "Forgot Password",borderwidth=0, font = ("times new roman",15,"bold"), relief=RIDGE, fg = "white" , bg = "black", activeforeground="white", activebackground="black")
        registerbtn.place(x=28, y=500, width=170)


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

    def return_login(self):
        self.root.destroy()

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

        # # **********bg img*****
        # self.bg = ImageTk.PhotoImage(file=r"college_images\img15.jpeg")
        
        # lbl_bg = Label(self.root , image = self.bg)
        # lbl_bg.place(x = 0, y = 0, relwidth=1 , relheight=1 )

        # *****left img********
        # self.bg1 = ImageTk.PhotoImage(file=r"college_images\img15.jpeg")
        
        # lbl_left = Label(self.root , image = self.bg1)
        # lbl_left.place(x = 50, y = 100, width=470 , height=550 )


        # *****frame******
        frame = Frame(self.root, bg="white")
        frame.place(x = 600, y = 180,width=800, height= 650)

        register_lbl = Label(frame, text= "Register Here", font= ("times new roman",30,"bold") , fg="darkgreen" ,bg = "white")
        register_lbl.place(x= 260, y = 40)

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
        b1 = Button(frame,image= self.photoimage1,command= self.return_login,cursor="hand2", borderwidth=0)
        b1.place(x = 410, y= 520, width = 300)


if __name__ == "__main__":
    main()