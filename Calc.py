from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""

cal = Tk()

cal.title("Calculator\nMrNimawS")

operator = ""

text_input = StringVar()

txtDisplay = Entry(cal, textvariable=text_input, bd=30,insertwidth=4,justify='right').grid(columnspan=4)

##----##
btn0 = Button(cal,text='0', command=lambda:btnClick(0)).grid(row=4, column=0)
btn00 = Button(cal,text='00', command=lambda:btnClick(00)).grid(row=5, column=0)
btn1 = Button(cal,text='1', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal,text='2', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal,text='3', command=lambda:btnClick(3)).grid(row=3, column=2)
btn4 = Button(cal,text='4', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal,text='5', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal,text='6', command=lambda:btnClick(6)).grid(row=2, column=2)
btn7 = Button(cal,text='7', command=lambda:btnClick(7) ).grid(row=1, column=0)
btn8 = Button(cal,text='8', command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal,text='9', command=lambda:btnClick(9)).grid(row=1, column=2)
##----##
dat = root = Button(cal,text='.', command=lambda:btnClick('.')).grid(row=5, column=3)
root = Button(cal,text='√', command=lambda:btnClick('**[1/2]')).grid(row=5, column=1)
power = Button(cal,text='^', command=lambda:btnClick('**')).grid(row=5, column=2)
addition = Button(cal,text='+', command=lambda:btnClick('+')).grid(row=1, column=3)
division = Button(cal,text='/', command=lambda:btnClick('/')).grid(row=4, column=3)
subtraction = Button(cal,text='-', command=lambda:btnClick('-')).grid(row=2, column=3)
multiply = Button(cal,text='*', command=lambda:btnClick('*')).grid(row=3, column=3)
##----##
btnClear = Button(cal,text='C', command= btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(cal,text='=', command=btnEqualsInput).grid(row=4, column=2)


cal.mainloop()