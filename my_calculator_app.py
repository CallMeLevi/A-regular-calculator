from tkinter import *
from tkinter.ttk import *

def write(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ''
    equation.set('')


def compute():
    try:
        global expression
        answer = str(eval(expression))
        equation.set(answer)
        expression = ''
    except:
        equation.set('error')
        expression = ''
       


window = Tk()
window.title('My Calculator app(Dudgital)')
window.geometry('500x500')


equation = StringVar()
expression = ''

screen = Entry(window, textvariable=equation)
btn_1 = Button(window, text='1', command = lambda:write(1))
btn_2 = Button(window, text='2', command = lambda:write(2))
btn_3 = Button(window, text='3', command = lambda:write(3))
btn_4 = Button(window, text='4', command = lambda:write(4))
btn_5 = Button(window, text='5', command = lambda:write(5))
btn_6 = Button(window, text='6', command = lambda:write(6))
btn_7 = Button(window, text='7', command = lambda:write(7))
btn_8 = Button(window, text='8', command = lambda:write(8))
btn_9 = Button(window, text='9', command = lambda:write(9))
btn_0 = Button(window, text='0', command = lambda:write(0))
btn_decimal = Button(window, text='.', command = lambda:write('.'))
btn_plus = Button(window, text='+', command = lambda:write('+'))
btn_mult = Button(window, text='X', command = lambda:write('*'))
btn_div = Button(window, text='/', command = lambda:write('/'))
btn_clear = Button(window, text='Clear', command=clear)
btn_equal = Button(window, text='=', command=compute)


screen.grid(columnspan=4, ipadx=70)
btn_1.grid(column=0, row=1)
btn_2.grid(column=1, row=1)
btn_3.grid(column =2, row=1)
btn_4.grid(column =0, row=2)
btn_5.grid(column =1, row=2)
btn_6.grid(column =2, row=2)
btn_7.grid(column =0, row=3)
btn_8.grid(column =1, row=3)
btn_9.grid(column =2, row=3)
btn_0.grid(column =1, row=4)
btn_decimal.grid(column =0, row=4)
btn_div.grid(column =3, row=3)
btn_mult.grid(column =3, row=2)
btn_plus.grid(column =3, row=1)
btn_equal.grid(column =3, row=4)
btn_clear.grid(column =2, row=4)




window.mainloop()
