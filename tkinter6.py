from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Learn tkinter")

frame=LabelFrame(root,padx=5,pady=5)
frame.pack(padx=10,pady=10)
myButton1 = Button(frame,text="Don't Click here")
myButton2 = Button(frame,text="or here")
myButton1.grid(row=0,column=0)
myButton2.grid(row=1,column=1)
root.mainloop()