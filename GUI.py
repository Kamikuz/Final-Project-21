import tkinter
import requests
import json
from tkinter import *
      
root = Tk()

menu = Menu(root) 
root.config(menu=menu)
root.geometry('500x300')
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Coming Soon')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

Label(root, text='Original Currency').grid(row=0) 
Label(root, text='Convert Currency').grid(row=1)
Label(root, text='Amount').grid(row=2)
e1 = Entry(root) 
e2 = Entry(root)
e3 = Entry(root)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

button = tkinter.Button(root,text='Submit',width=25)


mainloop()