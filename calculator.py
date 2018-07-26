from tkinter import *
import tkinter.messagebox
from tkinter import ttk


def msg(i):
    global txtResult
    # txtResult['text']=txtResult.get() + str(i)
    # .insert(-1,str(i))
    txtResult.insert(len(txtResult.get()), str(i))


root = Tk()
btn = []
txtResult = ttk.Entry(root, font=('arial', 12))
txtResult.grid(row=0, column=0, columnspan=3)
txtResult.config(justify = RIGHT)
for i in range(10):
    r = int(((i + 10) % 11) / 3) + 1
    c = ((i + 10) % 11) % 3
    btn.append(ttk.Button(root, text=str(i % 10)))
    btn[i].grid(row=r, column=c)
    btn[i]['width'] = 5
    btn[i]['padding'] = 10
    btn[i].config(command=lambda arg1=i: msg(arg1))
root.mainloop()
