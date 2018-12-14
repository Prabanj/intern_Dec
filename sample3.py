# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:02:29 2018

@author: Admin
"""
import serial
import tkinter
#import tkinter as tk
#import pyqrcode

#from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
#from ttk import Frame, Style



class simpleapp_tk(tkinter.Tk):
    
    
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.maxsize(width=35000, height=25000)
        
        

    def initialize(self):
        self.grid()
        self.entryVariable1 = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable1)
        self.entry.grid(column=1,row=3,sticky='W')
        
        
        
        button = tkinter.Button(self,text=u"Scan",command=self.OnButtonClick)
        button.grid(column=2,row=4)
        #self.initialize()
        button2 = tkinter.Button(self,text=u"Clear",command=self.OnButtonClick2)
        button2.grid(column=3,row=4)
        
        
        self.labelVariable2 = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable2,anchor="w",fg="white",bg="blue", bd = 15)
        label.grid(column=1,row=0,sticky='W')
        self.labelVariable2.set(u"UID Scanner")
        
        
    def OnButtonClick2(self):

        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        self.entry.delete(0,"end")
       #self.entryVariable1.set(s.readline())
       
        
    def OnButtonClick(self):
        self.s= serial.Serial()
        self.s.port = 'COM10'
        self.s.open()
        self.entryVariable1.set(self.s.readline())
        
        
      
if __name__ == "__main__":  
    
    app = simpleapp_tk(None)
    app.title('UID Scanner')
#    if s.readline():
#        simpleapp_tk(None)
    app.mainloop()