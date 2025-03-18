from tkinter import *

root = Tk()
root.title("Simple Calculator")
def button_click(number):
    # inputBox.delete(0,END)
    current=inputBox.get()
    inputBox.delete(0,END)
    inputBox.insert(0,str(current) + str(number))
    return
def button_clear():
    inputBox.delete(0,END)
inputBox = Entry(root,width=35,borderwidth=5)
def button_add():
    first_number = inputBox.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    inputBox.delete(0,END)
def button_equal():
    second_number = inputBox.get()
    inputBox.delete(0,END)
    if(math=="addition"):
        inputBox.insert(0,f_num+int(second_number))
    elif(math=="subtraction"):
        inputBox.insert (0,f_num-int(second_number))  
    elif(math=="multiplication"):
        inputBox .insert(0,f_num*int(second_number))
    elif(math=="division"):
        inputBox.insert(0,f_num/int(second_number))
def button_minus():
    first_number = inputBox.get()
    global f_num
    global math
    math ="subtraction"
    f_num = int(first_number)
    inputBox.delete(0,END)
def button_multiply():
    first_number = inputBox.get()
    global f_num
    global math
    math ="subtraction"
    f_num = int(first_number)
    inputBox.delete(0,END)
def button_multiply():
    first_number = inputBox.get()
    global f_num
    global math
    math ="multiplication"
    f_num = int(first_number)
    inputBox.delete(0,END)
def button_division():
    first_number = inputBox.get()
    global f_num
    global math
    math ="division"
    f_num = int(first_number)
    inputBox.delete(0,END)


myButton1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
myButton2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
myButton3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
myButton4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
myButton5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
myButton6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
myButton7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
myButton8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
myButton9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))

myButton0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
myButtonPlus = Button(root,text="+",padx=40,pady=20,command=button_add)

myButtonMinus = Button(root,text="-",padx=40,pady=20,command=button_minus)
myButtonMultiplication = Button(root,text="x",padx=40,pady=20,command=button_multiply)
myButtonDivision = Button(root,text="/",padx=40,pady=20,command=button_division)


myButtonclear = Button(root,text="clear",padx=80,pady=20,command=button_clear)
myButtonequal = Button(root,text="=",padx=80,pady=20,command=button_equal)

inputBox.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

myButton7.grid(row=1,column=0)
myButton8.grid(row=1,column=1)
myButton9.grid(row=1,column=2)

myButton4.grid(row=2,column=0)
myButton5.grid(row=2,column=1)
myButton6.grid(row=2,column=2)

myButton1.grid(row=3,column=0)
myButton2.grid(row=3,column=1)
myButton3.grid(row=3,column=2)

myButton0.grid(row=4,column=0)
myButtonclear.grid(row=4,column=1,columnspan=2)

myButtonPlus.grid(row=5,column=0)
myButtonequal.grid(row=5,column=1,columnspan=2)

myButtonMinus.grid(row=6,column=0)
myButtonMultiplication.grid(row=6,column=1)
myButtonDivision.grid(row=6,column=2)

root.mainloop()