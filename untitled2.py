# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:06:34 2018

@author: Admin
"""

from tkinter import *
from tkinter import ttk
gui = Tk()
gui.geometry("400x400")
#make sure first is capital and second is not
gui.title("UID Scanner")
a = Label(gui ,text="Decoded value").grid(row=0,column = 0)

e = Entry(gui).grid(row=0,column=1)

c.clear_button = gui.Button(self, text="Clear text", command=c.clear_text)
c.clear_button.pack()
gui.mainloop()