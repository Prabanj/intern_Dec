# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:51:18 2018

@author: Admin
"""


import serial
import tkinter

#import tkinter as tk
#import pyqrcode

from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
#from ttk import Frame, Style



class simpleapp_tk(tkinter.Tk):
    
    
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent

        self.initialize()
        self.maxsize(width=50000, height=50000)
        
        

    def initialize(self):

        self.grid()
        
        self.img = ImageTk.PhotoImage(Image.open('logo.jpg'))
        self.panel = tkinter.Label(image = self.img)
        self.panel.grid(row=0, column=0, columnspan=4)
        
        self.entryVariable1 = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable1)
        self.entry.grid(row=3, column=0, columnspan=2)
        
        
        
        button = tkinter.Button(self,text=u"Scan",command=self.OnButtonClick)
        button.grid(row=3, column=2)
        #self.initialize()
        button2 = tkinter.Button(self,text=u"Clear",command=self.OnButtonClick2)
        button2.grid(row=3, column=3)
        
        
        self.labelVariable2 = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable2,anchor="w",font="Corbel 15",fg="black", bg="white",height =0, bd = 4, justify="center")
        label.grid(row=2,column=0,columnspan =5)
        self.labelVariable2.set(u"Backcase Number")
        
        self.labelVariable3 = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable3,anchor="w",fg="#6a696f",bg="white",font="Consolas 20",height=0, bd=4, justify="center")
        label.grid(row=5,column=0,columnspan=5)
       
        
    def OnButtonClick2(self):

        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        self.entry.delete(0,"end")
       #self.entryVariable1.set(s.readline())
       
        
    def OnButtonClick(self):
        self.s= serial.Serial()
        self.s.port = 'COM10'
        self.s.open()
        self.a=self.s.readline()
        self.entryVariable1.set(self.a)
        self.labelVariable3.set(self.a)
#        print('a')
        
      

if __name__ == "__main__":  
    
    app = simpleapp_tk(None)
    app.title('UID Scanner')
    app.configure(bg='#fff')

#    if s.readline():
#        simpleapp_tk(None)
    app.mainloop()