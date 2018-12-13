# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:19:21 2018

@author: Admin
"""

from tkinter import*

gui=Tk()
gui.geometry("400x400")
#make sure first is capital and second is not
gui.title("UID Scanner")
a = Label(gui,text="Decoded value").grid(row=0,column = 0)


def e1_delete():
    e1.delete(first=0,last=22)

a=Entry(master, width=20)
a.pack()

B=Button(master, text="Submit", command=e1_delete())
B.pack()

master.mainloop