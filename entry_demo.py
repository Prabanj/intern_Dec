# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:17:18 2018

@author: Guest1
"""

from tkinter import *
master = Tk() 
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
mainloop() 