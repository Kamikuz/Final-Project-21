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

button = tkinter.Button(root,text='Submit',width=25,command=request)

def request():
	post_data = {'appid':'01b615dcc108bd15c022160f14627541'}
	post_data['form'] = x
	post_data['to'] = y
	response = requests.get('https://api.shenjian.io/exchange/currency',post_data)
	response = response.json()
	RATE = response['data']['rate']
	RATE = float(RATE)
	z = float(z)
	target_num = z * RATE
	Result = "--------Result--------\nOriginal Currency:"+x+"\nConvert Currency:"+y+target_num+"\nThe rate is:"+RATE+"\n----------------------"
	messageVar = Message(root, text = Result) 
	messageVar.config(bg='lightgreen') 
	messageVar.pack( )
	return

mainloop()