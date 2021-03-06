from tkinter import *
from PIL import Image
from tkinter import filedialog
import os
import cv2


f="image\pre.jpg"
root = Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

root.geometry("%dx%d" %(width,height))
#root.geometry("550x300+300+150")
root.configure(bg = '#6699ff')
root.resizable(width=True, height=True)
lbl=Label(root,text=" HANDWRITING RECOGNITION  SYSTEM" ,font=("Times new roman Bold",51))
lbl.grid(column=5,row=1)
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    rgb_im = img.convert('RGB')
    rgb_im.save(f)
    idd = cv2.imread(f,0)
    ims=cv2.resize(idd, (960, 540))
    cv2.imshow("Converted Image",ims)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #os.system('2.preprocessing.py')
   
btn = Button(root, text='Upload', command=open_img,bg="white",fg="red",font=30)
btn.place(relx=.2, rely=.5, anchor="c")



def a2():
    os.system('2.preprocessing.py')

btn2 = Button(root, text='Preprocessing' ,command=a2,bg="white",fg="red",font=30)
btn2.place(relx=.5, rely=.5, anchor="c")
#mod 3
#def a3():
#    os.system('3.segmentation.py')
   
#btn3 = Button(root, text='Segmentation',command=a3,bg="white",fg="red",font=30)
#btn3.place(relx=.6, rely=.5, anchor="c")
#mod 4

#mod 5
def a5():
    os.system('5.prediction.py')
   
btn5 = Button(root, text='Prediction ',command=a5,bg="white",fg="red",font=30)
btn5.place(relx=.8, rely=.5, anchor="c")
#front.py
#Displaying front.py.
root.mainloop()
