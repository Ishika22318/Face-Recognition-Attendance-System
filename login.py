from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1090+0+0")

        self.bg = ImageTk.PhotoImage(file=r"college_images\img14.jpeg")

        lbl_bg = Label(self.root , image = self.bg)
        lbl_bg.place(x = 0, y = 0, relwidth=1 , relheight=1 )

        frame = Frame(self.root, bg = "black")
        frame.place(x=610, y = 170,width = 340, height = 450)

        img1 = Image.open(r"college_images\img14.jpeg")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        # lblimg1 = Label(image=self.photoimage1,bg = "black",borderwidth= )

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()