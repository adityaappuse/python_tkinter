from tkinter import *
from PIL import Image,ImageTk

root = Tk()

pizza=StringVar()
Modes = ["Pepperoni","Cheese","Mushroom","Onion"]
for mode in Modes:
    Radiobutton(root,text=mode,variable=pizza,value=mode).pack(anchor=W)

def buttonClick(value):
    myLabel = Label(root,text=value)
    myLabel.pack()

# Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:buttonClick(r.get())).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:buttonClick(r.get())).pack()

# myLabel = Label(root,text=pizza.get())
# myLabel.pack()
myButton = Button(root,text="Click here ",command=lambda:buttonClick(pizza.get()))
myButton.pack()

root.mainloop()