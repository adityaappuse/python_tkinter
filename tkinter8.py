from tkinter import *
from tkinter import messagebox
 
root = Tk()

root.title("Hello for coming")

def popup():
    response = messagebox.askyesno("This is my Popup!","Hello World")
    Label(root,text=response).pack()

myButton = Button(root,text="Popup",command=popup).pack()
root.mainloop()