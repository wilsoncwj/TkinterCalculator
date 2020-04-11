from tkinter import *
from tkinter import messagebox

cal = Tk()
cal.title("Calculator")

text_Input = StringVar()

screen = ""


def click(numbers):
    global screen                       # use nonlocal for nested functions, but now only got global as parent
    screen = screen + str(numbers)
    text_Input.set(screen)

def equals():
    global screen
    try:
        screen = str(eval(screen))
        text_Input.set(screen)
    except SyntaxError:
        messagebox.showinfo('ERROR','Invalid Operation!')
        clear()

def clear():
    global screen
    screen = ""
    text_Input.set(screen)

def quitcalc():
    raise SystemExit


txtDisplay = Entry(cal, font=('arial', 20, 'bold'), bd=10, textvariable=text_Input,     # bd is border width
                    bg="powder blue", justify='right', insertwidth=4)                   # insertwidth is the width of blinking cursor
txtDisplay.grid(row=0, columnspan=4)                                                    # let a widget span more than one column


### Buttons
# 1st row total width = 150
btn_clear = Button(cal, font=('arial', 20, 'bold'), text="CE", bd=5, bg="powder blue", fg="black", padx=60, command=lambda:clear())
btn_clear.grid(row=1, columnspan=2, sticky='nesw')

btn_power = Button(cal, font=('arial', 20, 'bold'), text="pow", bd=5, bg="powder blue", fg="black", padx=0, command=lambda:click("**"))
btn_power.grid(row=1, column=2, sticky='nesw')

btn_modulo = Button(cal, font=('arial', 20, 'bold'), text="%", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click("%"))
btn_modulo.grid(row=1, column=3, sticky='nesw')

#============================================================================================================================
# function lambda that takes nothing and returns click()
btn7 = Button(cal, font=('arial', 20, 'bold'), text="7", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(7))
btn7.grid(row=2, column=0, sticky='nesw')

btn8 = Button(cal, font=('arial', 20, 'bold'), text="8", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(8))
btn8.grid(row=2, column=1, sticky='nesw')

btn9 = Button(cal, font=('arial', 20, 'bold'), text="9", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(9))
btn9.grid(row=2, column=2, sticky='nesw')

btn_divide = Button(cal, font=('arial', 20, 'bold'), text="/", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click("/"))
btn_divide.grid(row=2, column=3, sticky='nesw')

#============================================================================================================================
btn4 = Button(cal, font=('arial', 20, 'bold'), text="4", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(4))
btn4.grid(row=3, column=0, sticky='nesw')

btn5 = Button(cal, font=('arial', 20, 'bold'), text="5", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(5))
btn5.grid(row=3, column=1, sticky='nesw')

btn6 = Button(cal, font=('arial', 20, 'bold'), text="6", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(6))
btn6.grid(row=3, column=2, sticky='nesw')

btn_multiply = Button(cal, font=('arial', 20, 'bold'), text="x", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click("*"))
btn_multiply.grid(row=3, column=3, sticky='nesw')

#============================================================================================================================
btn1 = Button(cal, font=('arial', 20, 'bold'), text="1", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(1))
btn1.grid(row=4, column=0, sticky='nesw')

btn2 = Button(cal, font=('arial', 20, 'bold'), text="2", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(2))
btn2.grid(row=4, column=1, sticky='nesw')

btn3 = Button(cal, font=('arial', 20, 'bold'), text="3", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(3))
btn3.grid(row=4, column=2, sticky='nesw')

btn_minus = Button(cal, font=('arial', 20, 'bold'), text="-", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click("-"))
btn_minus.grid(row=4, column=3, sticky='nesw')

#============================================================================================================================
btn0 = Button(cal, font=('arial', 20, 'bold'), text="0", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click(0))
btn0.grid(row=5, column=0, sticky='nesw')

btn_decimal = Button(cal, font=('arial', 20, 'bold'), text=".", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click("."))
btn_decimal.grid(row=5, column=1, sticky='nesw')

btn_equal = Button(cal, font=('arial', 20, 'bold'), text="=", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:equals())
btn_equal.grid(row=5, column=2, sticky='nesw')

btn_add = Button(cal, font=('arial', 20, 'bold'), text="+", bd=5, bg="powder blue", fg="black", padx=30, command=lambda:click("+"))
btn_add.grid(row=5, column=3, sticky='nesw')

btn_quit = Button(cal, font=('arial', 20, 'bold'), text="Quit", bd=5, bg="gold", fg="black", padx=150, command=lambda:quitcalc())
btn_quit.grid(row=6, columnspan=4, sticky='nesw')


try:
    cal.mainloop()
except KeyboardInterrupt:
    quit()