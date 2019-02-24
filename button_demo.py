# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:11:53 2018

@author: Guest1
"""

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("200x200")     # main window size
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python","Hi")      # messagebox

B = Button(top, text = "Hello", command = helloCallBack)    # button
B.place(x = 100,y = 100)    # button position
top.mainloop()