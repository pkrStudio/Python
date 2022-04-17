from cProfile import label
from cgitb import text
from tkinter import *
import tkinter
from tkinter.ttk import*

def button_command():
    print(UN.get())
    print(PW_1.get())
    print(PW_2.get())
    print('login sucess')

root = Tk()
root.title('gui program')
# root.geometry("400*400")

label(root,text="username").grid(row=4)
UN =Entry(root)
UN.grid(row=4 ,column=1)

Label(root,text="password_1").grid(row=4)
UN=Entry(root)
UN.grid(row=4,column=1)

