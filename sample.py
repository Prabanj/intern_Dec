# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 18:29:21 2018

@author: Guest1
"""

import Tkinter
import Tkinter as tk
import pyqrcode

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style




class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
#        self.minsize(width=466, height=466)
        self.maxsize(width=35000, height=25000)

    def initialize(self):
        self.grid()
        
        self.entryVariable1 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable1)
        self.entry.grid(column=1,row=3,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable1.set(u"")
        
        
        button6 = Tkinter.Button(self,text=u"Get as QR",
                                command=self.OnButtonClick6)
        button6.grid(column=4,row=28)
        
        
        self.labelVariable7 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable7,
                              anchor="w",fg="black",bg="violet", bd = 15)
        label.grid(column=3,row=0,columnspan=10,sticky='W')
        self.labelVariable7.set(u"iTitan - A Click Solution for Titan Eye Plus")
        
        
     def OnButtonClick2(self):
        #self.labelVariable.set( self.entryVariable.get()+" (clicked sumthin else didncha)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        
        
        
if __name__ == "__main__":  
    
    app = simpleapp_tk(None) 
    
    app.title('iTitan')
    app.mainloop()