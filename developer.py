from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1920, height=55)

        img_top = Image.open(r"college_images\developer1.jpeg")  # Insert Image inside ""
        img_top = img_top.resize((1920, 1090), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1920, height=1090)

        # ********Frame**********************
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=300, y=60, width=400, height=600)

        img_top1 = Image.open(r"college_images\developer1.jpeg")  # Insert Image inside ""
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

       

        # Developer info
        dev_label = Label(main_frame,text="Ishika Agarwal",  font=("times new roman", 20, "bold"))
        dev_label.place(x=125, y=15)

        dev_label = Label(main_frame, text="19ESKIT032", font=("times new roman", 20, "bold"))
        dev_label.place(x=130, y=55)

        dev_labe2 = Label(main_frame,text="Kritika Surana", font=("times new roman", 20, "bold"))
        dev_labe2.place(x=125, y=155)

        dev_labe2 = Label(main_frame, text="19ESKIT046", font=("times new roman", 20, "bold"))
        dev_labe2.place(x=130, y=195)

        dev_labe2 = Label(main_frame,  text="Kunal Bharagatiya", font=("times new roman", 20, "bold"))
        dev_labe2.place(x=125, y=295)

        dev_labe2 = Label(main_frame, text="19ESKIT048", font=("times new roman", 20, "bold"))
        dev_labe2.place(x=130, y=335)


        dev_labe2 = Label(main_frame,  text="Lavanya Jain",font=("times new roman", 20, "bold"))
        dev_labe2.place(x=125, y=435)

        dev_labe2 = Label(main_frame, text="19ESKIT051", font=("times new roman", 20, "bold"))
        dev_labe2.place(x=130, y=475)


        



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
