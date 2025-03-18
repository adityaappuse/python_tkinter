from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root,text="Yeah, click me more for more maybe",fg="navy blue",bg = "beige")
    myLabel.pack()

myButton = Button(root,text="Click me",padx=50,pady=50,command=myClick)

myButton.pack()

root.mainloop()

