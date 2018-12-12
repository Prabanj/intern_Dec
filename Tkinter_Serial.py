# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:06:01 2018

@author: Administrator
"""

import serial 
import pyperclip


# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk




ser = serial.Serial()
ser.port = 'COM8'
ser.open()
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
    a = ser.readline() 
    print(a)
#            
#    #self.labelVariable2.set(int(a[1:18]))
    #pyperclip.copy(a)