# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:20:09 2018

@author: Guest1
"""

import tkinter as tk

class Mainframe(tk.Frame):
    # Mainframe contains the widgets
    # More advanced programs may have multiple frames
    # or possibly a grid of subframes
    
    def __init__(self,master,*args,**kwargs):
        # *args packs positional arguments into tuple args
        # **kwargs packs keyword arguments into dict kwargs
        
        # initialise base class
        tk.Frame.__init__(self,master,*args,**kwargs)
        # in this case the * an ** operators unpack the parameters
        
        # put your widgets here
        self.value = tk.IntVar()
        tk.Label(self,textvariable = self.value).pack()
        self.TimerInterval = 500
        
        # variable for dummy GetTemp
        self.Temp = 0
        
        # call Get Temp which will call itself after a delay
        self.GetTemp()
        
    def GetTemp(self):
        ## replace this with code to read sensor
        self.value.set(self.Temp)
        self.Temp += 1
        
        # Now repeat call
        self.after(self.TimerInterval,self.GetTemp)
   
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
               
        # set the title bar text
        self.title('Demo')
        # Make sure app window is big enough to show title 
        self.geometry('300x100')
      
        # create and pack a Mainframe window
        Mainframe(self).pack()
        
        # now start
        self.mainloop()
                    
# create an App object
# it will run itself
App()