import serial
import tkinter as tk

s= serial.Serial()
s.port = 'COM8'
s.open()

class Mainframe(tk.Frame):
    
    
    def __init__(self,master,*args,**kwargs):
        
        tk.Frame.__init__(self,master,*args,**kwargs)
        self.value = tk.IntVar()
        tk.Label(self,textvariable = self.value).pack()
        self.TimerInterval = 5
        self.Temp = 0
        self.GetTemp()
        
        
        
    def GetTemp(self):
        
        self.value.set(self.Temp)
        self.Temp += 1
        self.after(self.TimerInterval,self.GetTemp)
        
        
   
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Demo')
        self.geometry('300x100')
        Mainframe(self).pack()
        self.mainloop()

App()