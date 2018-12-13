#import serial
import tkinter as tk
from PIL import ImageTk,Image

#s= serial.Serial()
#s.port = 'COM10'
#s.open()

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open('C:/Users/Guest1/Downloads/logo.jpg'))
panel = tk.Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "no")

w = tk.Canvas(root, width=400, height=60) 
w.pack() 
canvas_height=20
canvas_width=2000
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y )

w = tk.Label(root, text="UID Scanner") 
w.pack() 

#class Mainframe(tk.Frame):
#    
#    
#    def __init__(self,master,*args,**kwargs):
#        
#        tk.Frame.__init__(self,master,*args,**kwargs)
#        self.value = tk.IntVar()
#        tk.Label(self,textvariable = self.value).pack()
#        self.TimerInterval = 1
#        self.Temp = 0
#        self.GetTemp()
#        
#        
#        
#    def GetTemp(self):
#        
#        self.value.set(self.Temp)
#        #self.Temp += 1
#        self.Temp = s.readline()
#        self.after(self.TimerInterval,self.GetTemp)
#        
#        
#   
#class App(tk.Tk):
#    def __init__(self):
#        tk.Tk.__init__(self)
#        self.title('Demo')
#        self.geometry('300x100')
#        Mainframe(self).pack()
#        self.mainloop()
#
#App()

w = tk.Canvas(root, width=400, height=60) 
w.pack() 
canvas_height=20
canvas_width=2000
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y )


root.mainloop()