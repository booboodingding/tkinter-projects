from tkinter import*
import tkinter

root = Tk()

root.geometry("145x165")

equa = ""
equation = StringVar()

calculation = Label(root,textvariable=equation)

equation.set("Enter you equation")

calculation.grid(columnspan=4)

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def clearInput():
    global equa
    equa = ""
    equation.set(equa)

def equals():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""

def popInput():
    global equa
    delEqua = list(equa)
    delEqua.pop()
    equa = ''.join(delEqua)
    equation.set(equa)

Button0 = Button(root, text="0",command=lambda:btnPress(0))
Button1 = Button(root, text="1",command=lambda:btnPress(1))
Button2 = Button(root, text="2",command=lambda:btnPress(2))
Button3 = Button(root, text="3",command=lambda:btnPress(3))
Button4 = Button(root, text="4",command=lambda:btnPress(4))
Button5 = Button(root, text="5",command=lambda:btnPress(5))
Button6 = Button(root, text="6",command=lambda:btnPress(6))
Button7 = Button(root, text="7",command=lambda:btnPress(7))
Button8 = Button(root, text="8",command=lambda:btnPress(8))
Button9 = Button(root, text="9",command=lambda:btnPress(9))

Button0.grid(row=1,column=0)
Button1.grid(row=1,column=1)
Button2.grid(row=1,column=2)
Button3.grid(row=2,column=0)
Button4.grid(row=2,column=1)
Button5.grid(row=2,column=2)
Button6.grid(row=3,column=0)
Button7.grid(row=3,column=1)
Button8.grid(row=3,column=2)
Button9.grid(row=4,column=1)

Plus = Button(root, text="+",command=lambda:btnPress("+"))
Plus.grid(row=1,column=3)
Minus = Button(root, text="-",command=lambda:btnPress("-"))
Minus.grid(row=2,column=3)
Divide = Button(root, text="/",command=lambda:btnPress("/"))
Divide.grid(row=3,column=3)
Multiply = Button(root, text="*",command=lambda:btnPress("*"))
Multiply.grid(row=4,column=3)
Equals = Button(root, text="=",command=equals)
Equals.grid(row=4,column=2)
Clear = Button(root,text="c",command=lambda:clearInput())
Clear.grid(row=4,column=0)
Del = Button(root,text="del",command=popInput)
Del.grid(row=5,columnspan=4)




root.mainloop()
