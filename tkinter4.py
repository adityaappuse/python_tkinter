from tkinter import *

root = Tk()

e = Entry(root,width=50,fg="#F1DABF",bg="#60463b",borderwidth=4)
e.pack()
e.insert(0,"Enter your name :")
def takeInput():
    myLabel = Label(root,text=f"Hello {e.get()}")
    myLabel.pack()
myButton = Button(root,text="Click for output",command=takeInput)
myButton.pack()


root.mainloop()