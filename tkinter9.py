from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

root = Tk()
root.title("Image viewer")

def open_image():
    global my_Image
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\adity\Documents\experiment",title="Select the files",filetypes=[("all files","*.*")])
    my_Label = Label(root,text=root.filename).pack()
    my_Image = ImageTk.PhotoImage(Image.open(root.filename))
    my_Image_Label = Label(image=my_Image,height=200,width=200).pack()


my_button = Button(root,text="Open now",command=open_image).pack()

root.mainloop()