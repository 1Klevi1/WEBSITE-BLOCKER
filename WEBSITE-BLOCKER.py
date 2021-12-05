
from tkinter import *
from tkinter import ttk
import tkinter

window=Tk()
window.geometry('900x600')
window.resizable(0,0)
window.title("'Klevi's -Website Blocker")

Label(window, text ='WEBSITE BLOCKER' , font ='arial 20 bold').pack()
Label(window, text ='Klevi' , font ='arial 20 bold').pack(side=BOTTOM)

host_path =r'C:\Users\E-store\OneDrive\Desktop\Yotube video'
ip_address = '127.0.0.1'
Label(window, text ='Enter Website :' , font ='arial 13 bold').place(x=5 ,y=60)
Websites = Text(window,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x= 140,y = 60)
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(window, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(window, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

block = Button(window, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')

block.place(x = 230, y = 150)
window.mainloop() 
