from tkinter import *
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
        self.root.geometry("2366x1768+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=50)


        img_top=Image.open(r"images\face_recognition2.jpeg") 
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)               
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325) 


        # button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1370,height=60)

        img_bottom=Image.open(r"images\face_recognition2.jpeg") 
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)               
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            if cv2.waitKey(1) & 0xFF == 13:  # Check for Enter key press
                break

        # Convert ids to a NumPy array
        ids = np.asarray(ids)

        # ===== TRAIN THR CLASSIFIER AND SAVE =====
        clf = cv2.face.LBPHFaceRecognizer_create() 
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")







if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()