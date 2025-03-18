from tkinter import *
from PIL import ImageTk,Image
root = Tk()

root.title("Test file for further projects")
root.iconbitmap(r"C:\Users\adity\Downloads\Archivos_25593.ico")

my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\adity\Pictures\wallhaven-gpedg3.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\adity\Pictures\wallhaven-3krojd.png"))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\adity\Pictures\wallhaven-9dlyyd.png"))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\adity\Pictures\wallhaven-rrljjq.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\adity\Pictures\aditya.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_Label=Label(image=my_img1,height=500 ,width=500)
my_Label.grid(row=0,column=0,columnspan=3)

status=Label(root,text=f"Image 1 of {len(image_list)}",bd=1,relief=SUNKEN,anchor=E)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def previous_Image(image_num):
    global my_Label
    global button_next
    global button_previous
   
    my_Label.grid_forget()
   
    my_Label = Label(image=image_list[image_num],height=500,width=500)
    button_next = Button(root,text=">>",command=lambda: next_Image(image_num+1))
    
    button_previous = Button(root,text="<<",command=lambda: previous_Image(image_num-1))
    if(image_num<=0):
        button_previous = Button(root,text="<<",state=DISABLED)
    my_Label.grid(row=0,column=0,columnspan=3)
    button_previous.grid(row=1,column=0)
    button_quit.grid(row=1,column=1)
    button_next.grid(row=1,column=2)
                            

    
def next_Image(image_num):
    global my_Label
    global button_next
    global button_previous

    

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_num],height=500,width=500)
    button_next = Button(root,command=lambda: next_Image(image_num+1))
    if(image_num == 4):
        button_next = Button(root,text=">>",state=DISABLED)
    button_previous = Button(root,command=lambda:next_Image(image_num-1))
    if(image_num<=0):
        button_previous = Button(root,text="<<",state=DISABLED)

    my_Label.grid(row=0,column=0,columnspan=3)
    button_previous.grid(row=1,column=0)
    button_quit.grid(row=1,column=1)
    button_next.grid(row=1,column=2)

    status=Label(root,text=f"Image {image_num+1} of {len(image_list)}",bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

button_previous = Button(root,text="<<")
button_next = Button(root,text=">>",command=lambda:next_Image(1))
button_quit= Button(root,text="Exit the screen",command=root.quit)

button_previous.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_next.grid(row=1,column=2)

root.mainloop()