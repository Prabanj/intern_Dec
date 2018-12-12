# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:06:01 2018

@author: Administrator
"""

import serial 
import pyperclip
import Tkinter
from Tkinter import *


# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk




s = serial.Serial()
s.port = 'COM8'
s.open()
#while True:
#    a = ser.readline() 
#    print(int(a[1:18]))
#            
#    #self.labelVariable2.set(int(a[1:18]))
#    pyperclip.copy(int(a[2:16]))

#a = ser.readline() 
#print(a)
#            
# #self.labelVariable2.set(int(a[1:18]))
#pyperclip.copy(int(a[2:16]))

while True:
    a = s.readline() 
    print(a)
    
#            
#    #self.labelVariable2.set(int(a[1:18]))
    #pyperclip.copy(a)
    
    
    import serial

#s = serial.Serial('COM10',9600)    # open serial port
master = Tk()
master.geometry("1360x750")        # a window pop up with width (1360) and height(750)     which exatly fits my monitor screen..

while 1:
if s.inWaiting():
text = s.readline(s.inWaiting())
frameLabel = Frame( master, padx=40, pady =40)
frameLabel.pack()
w = Text( frameLabel, wrap='word', font="TimesNewRoman 37")
w.insert(12.0,text )
w.pack()
w.configure( bg=master.cget('bg'), relief='flat', state='Normal' )

mainloop()