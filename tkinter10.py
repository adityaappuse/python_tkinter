from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Slider something")
root.geometry("400x400")

vertical = Scale(root,from_=0,to=400)
vertical.pack()

horizontal = Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_Label = Label(root,text=str(vertical.get()) +"x"+str(horizontal.get())).pack()
    root.geometry(str(horizontal.get()) + "x" +str(vertical.get()))
my_Button = Button(root,text="Click me",command=slide).pack()

root.mainloop()