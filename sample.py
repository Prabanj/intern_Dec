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
        self.entryVariable1.set(u"")
        
        
        button = tkinter.Button(self,text=u"Clear",command=self.OnButtonClick)
        button.grid(column=2,row=4)
        button2 = tkinter.Button(self,text=u"Copy",command=self.OnButtonClick2)
        button2.grid(column=3,row=4)
        
        
        self.labelVariable2 = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable2,anchor="w",fg="white",bg="blue", bd = 15)
        label.grid(column=1,row=0,sticky='W')
        self.labelVariable2.set(u"UID Scanner")
        
        
    def OnButtonClick(self):

        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        self.entry.delete(0,"end")

        
    def OnButtonClick2(self):
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        
        
        
if __name__ == "__main__":  
    
    app = simpleapp_tk(None) 
    app.title('UID Scanner')
    app.mainloop()