from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1920,height=45)

        # img_top = Image.open(r"college_images\img2.jpeg")  # Insert Image inside ""
        # img_top = img_top.resize((1920, 325), Image.ANTIALIAS)
        # self.photoimg_top = ImageTk.PhotoImage(img_top)

        img = Image.open(r"college_images\img1.jpeg")
        img = img.resize((480,250),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=480,height=250)

        # second image
        img1 = Image.open(r"college_images\img3.jpeg")
        img1 = img1.resize((480,250),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=480,y=0,width=480,height=250)

        # third image
        img2 = Image.open(r"college_images\img4.jpeg")
        img2 = img2.resize((480,250),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=960,y=0,width=480,height=250)


        # fourth image
        img3 = Image.open(r"college_images\img5.jpeg")
        img3 = img3.resize((480,250),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image = self.photoimg3)
        f_lbl.place(x=1440,y=0,width=480,height=250)

        # button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1920, height=60)

        img_bottom = Image.open(r"college_images\img25.jpeg")
        img_bottom = img_bottom.resize((1920, 425), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1920, height=525)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ============== Train the classifier and Save ================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()