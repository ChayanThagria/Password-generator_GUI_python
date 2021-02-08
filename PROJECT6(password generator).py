from tkinter import *
import random

root = Tk()
root.geometry("600x100")
root.title("password generator")
values = [i for i in "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"]

Label(text = "enter length of password").pack(side = TOP)

scvalue = StringVar()
scvalue.set("")
screen = Entry(textvariable = scvalue)
screen.pack(ipadx = 200)
a=[]

def basic():
    n = int(screen.get())
    generate(n)

def generate(n):
    for i in range(n):
        a.append(random.choice(values))
    final = "".join(a)
    scvalue.set(final)
    screen.update()

Button(text = "Generate",command = basic).pack()

root.mainloop()

