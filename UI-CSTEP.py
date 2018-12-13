# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:11:36 2016

@author: Guest1
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 15:20:41 2016

@author: Guest1
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:56:52 2016

@author: Guest1
"""

import numpy as np
import pyqrcode
import cv2
import math
import Tkinter
import Tkinter as tk
import pyqrcode

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style


from openpyxl.workbook import Workbook

refPt = []
refPtlist=[]
cropping = False

global B
global pd
global A
global DBL
global FD
global SP_R
global Name
global pd_L
global pd_R
global minthickness


class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
#        self.minsize(width=466, height=466)
        self.maxsize(width=35000, height=25000)

    def initialize(self):
        self.grid()
#        self.pack(fill=BOTH, expand=1)
        
    # Name enter
        self.entryVariable1 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable1)
        self.entry.grid(column=1,row=3,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable1.set(u"")
    # Age enter   
        self.entryVariable2 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable2)
        self.entry.grid(column=1,row=4,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable2.set(u"")
    # Gender enter
        self.entryVariable3 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable3)
        self.entry.grid(column=1,row=5,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable3.set(u"")
    # S power enter   
        self.entryVariable4 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable4)
        self.entry.grid(column=1,row=9,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable4.set(u"")
        
        
    # C power enter  
        self.entryVariable5 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable5)
        self.entry.grid(column=1,row=10,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable5.set(u"")
        
        
    # Axis enter  
        self.entryVariable6 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable6)
        self.entry.grid(column=1,row=11,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable6.set(u"")
        
        #Right eye
    # S power enter   
        self.entryVariable9 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable9)
        self.entry.grid(column=3,row=9,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable9.set(u"")
        self.pack_propagate(0)
        
    # C power enter  
        self.entryVariable10 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable10)
        self.entry.grid(column=3,row=10,sticky='E')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable10.set(u"")
        
    # Axis enter  
        self.entryVariable11 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable11)
        self.entry.grid(column=3,row=11,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable11.set(u"")

    #Comparing thickness
        self.entryVariable12 = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable12)
        self.entry.grid(column=10,row=4,columnspan=2,sticky='W')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable12.set(u"")
        
   # RI Selection
        lst1 = ['CR39 1.498','Crown Glass 1.523','Glass 1.56','Glass 1.7','Glass 1.8','Glass 1.9','Polycarbonate 1.586','Trivex 1.532','Plastics 1.56','Plastics 1.60','Plastics 1.67','Plastics 1.74']
        self.var1 = Tkinter.StringVar()
        self.list1 = Tkinter.OptionMenu(self,self.var1,*lst1)
        self.list1.grid(column=1,row=13,columnspan=6,sticky='W')
        
        lst6 = ['40 CM','50 CM','60 CM','70 CM','80 CM','90 CM']
        self.var6 = Tkinter.StringVar()
        self.list6 = Tkinter.OptionMenu(self,self.var6,*lst6)
        self.list6.grid(column=3,row=13,columnspan=6,sticky='W')
        
 

    #Measure PD   
        button2 = Tkinter.Button(self,text=u"Measure PD",
                                command=self.OnButtonClick2)
        button2.grid(column=1,row=15)
    # NMeaure Frame    
        button3 = Tkinter.Button(self,text=u"Measure FRAME",
                                command=self.OnButtonClick3)
        button3.grid(column=2,row=15)
        
        button4 = Tkinter.Button(self,text=u"Calc Thickness",
                                command=self.OnButtonClick4)
        button4.grid(column=0,row=28)
        
        button5 = Tkinter.Button(self,text=u"Measure FD",
                                command=self.OnButtonClick5)
        button5.grid(column=3,row=15)
        #QR code
        button6 = Tkinter.Button(self,text=u"Get as QR",
                                command=self.OnButtonClick6)
        button6.grid(column=4,row=28)
        
#        button7 = Tkinter.Button(self,text=u"Click to see Lens Type ",
#                                command=self.OnButtonClick4)
#        button7.grid(column=3,row=23)
#        
        button8 = Tkinter.Button(self,text=u"Reset Input",
                                command=self.OnButtonClick8)
        button8.grid(column=1,row=28)
        
        button9 = Tkinter.Button(self,text=u"Reset Output",
                                command=self.OnButtonClick9)
        button9.grid(column=2,row=28)
        
        button10 = Tkinter.Button(self,text=u"Save Details",
                                command=self.OnButtonClick10)
        button10.grid(column=3,row=28)
        
        button11 = Tkinter.Button(self,text=u"View Lens Thickness",
                                command=self.OnButtonClick11)
        button11.grid(column=7,row=17)
 #Test Inputs       
        button12 = Tkinter.Button(self,text=u"Clear Plot",
                                command=self.OnButtonClick12)
        button12.grid(column=9,row=17,columnspan=5,sticky='e')
#        
#        button13 = Tkinter.Button(self,text=u"Test Inputs 2 ",
#                                command=self.OnButtonClick13)
#        button13.grid(column=1,row=24)
#        
#        button14 = Tkinter.Button(self,text=u"Test Inputs 3 ",
#                                command=self.OnButtonClick14)
#        button14.grid(column=2,row=24)
#        
#        button15 = Tkinter.Button(self,text=u"Test Inputs 4 ",
#                                command=self.OnButtonClick15)
#        button15.grid(column=3,row=24)
        
        button16 = Tkinter.Button(self,text=u"Compare Lenses",
                                command=self.OnButtonClick16)
        button16.grid(column=10,row=17,columnspan=5,sticky='w')
        
#        self.labelVariable7 = Tkinter.StringVar()
#        label = Tkinter.Label(self,textvariable=self.labelVariable7,
#                              anchor="w",fg="red",bg="violet", bd = 20)
#        label.grid(column=8,row=40,columnspan=10,sticky='W')
#        self.labelVariable7.set(u"iTitan - A Click Solution for Titan Eye Plus")
#        
        
#        
        
        self.labelVariable7 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable7,
                              anchor="w",fg="black",bg="violet", bd = 15)
        label.grid(column=3,row=0,columnspan=10,sticky='W')
        self.labelVariable7.set(u"iTitan - A Click Solution for Titan Eye Plus")
        
        self.labelVariable72 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable72,
                              anchor="w",fg="white",bg="white")
        label.grid(column=0,row=1,columnspan=5,sticky='W')
        self.labelVariable72.set(u"Spacer for Customer Details")
        
        self.labelVariable8 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable8,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=2,columnspan=5,sticky='W')
        self.labelVariable8.set(u"Customer Details")
        
        self.labelVariable9 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable9,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=3,columnspan=5,sticky='W')
        self.labelVariable9.set(u"Name:")
        
        self.labelVariable10 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable10,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=4,columnspan=6,sticky='W')
        self.labelVariable10.set(u"Age:")

        self.labelVariable11 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable11,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=5,columnspan=5,sticky='W')
        self.labelVariable11.set(u"Gender:")
 #Spacer       
        self.labelVariable70 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable70,
                              anchor="w",fg="white",bg="white")
        label.grid(column=0,row=6,columnspan=5,sticky='W')
        self.labelVariable70.set(u"         ")
        
        self.labelVariable12 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable12,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=7,columnspan=5,sticky='W')
        self.labelVariable12.set(u"Power Details")
        
        self.labelVariable52 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable52,anchor="e",fg="WHITE",bg="white")
        label.grid(column=0,row=22,columnspan=1,sticky='W')
        self.labelVariable52.set(u"Spherical power   ")
        
        self.labelVariable47 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable47,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=8,columnspan=5,sticky='W')
        self.labelVariable47.set(u"Left Eye")
        
        self.labelVariable48 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable48,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=2,row=8,columnspan=5,sticky='W')
        self.labelVariable48.set(u"Right Eye")
    #SP L    
        self.labelVariable13 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable13,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=9,columnspan=5,sticky='W')
        self.labelVariable13.set(u"Spherical Power")
        
        self.labelVariable14 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable14,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=10,columnspan=5,sticky='W')
        self.labelVariable14.set(u"Cylindrical Power")
        
        self.labelVariable15 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable15,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=11,columnspan=5,sticky='W')
        self.labelVariable15.set(u" Axis")
        
        self.labelVariable49 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable49,
                              anchor="w",fg="black",bg="white")
        label.grid(column=2,row=9,columnspan=5,sticky='W')
        self.labelVariable49.set(u"Spherical Power")
        
        self.labelVariable50 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable50,
                              anchor="w",fg="black",bg="white")
        label.grid(column=2,row=10,columnspan=5,sticky='W')
        self.labelVariable50.set(u"Cylindrical Power")
        
        self.labelVariable51 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable51,
                              anchor="w",fg="black",bg="white")
        label.grid(column=2,row=11,columnspan=5,sticky='W')
        self.labelVariable51.set(u"Axis")
        
#Spacer - Axis to Choose lens        
        self.labelVariable71 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable71,
                              anchor="w",fg="white",bg="white")
        label.grid(column=0,row=12,columnspan=5,sticky='W')
        self.labelVariable71.set(u"         ")
        
        self.labelVariable16 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable16,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=13,columnspan=5,sticky='W')
        self.labelVariable16.set(u"Choose Lens")
        
        self.labelVariable16 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable16,
                              anchor="w",fg="black",bg="white")
        label.grid(column=2,row=13,columnspan=5,sticky='W')
        self.labelVariable16.set(u"Choose Distance")
        
        self.labelVariable75 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable75,
                              anchor="w",fg="white",bg="white")
        label.grid(column=0,row=14,columnspan=5,sticky='W')
        self.labelVariable75.set(u"Spacer below drop")
        
        self.labelVariable76 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable76,
                              anchor="w",fg="white",bg="white")
        label.grid(column=0,row=14,columnspan=5,sticky='W')
        self.labelVariable76.set(u"Spacer side to buttons")
        
#Spacer below m. buttons   
        self.labelVariable74 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable74,
                              anchor="w",fg="white",bg="white")
        label.grid(column=0,row=16,columnspan=5,sticky='W')
        self.labelVariable74.set(u"        ")
  
        self.labelVariable23 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable23,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=17,columnspan=5,sticky='W')
        self.labelVariable23.set(u"The Measured parameters are ")
        
#        self.labelVariable17 = Tkinter.StringVar()
#        label = Tkinter.Label(self,textvariable=self.labelVariable17,
#                              anchor="w",fg="black",bg="white")
#        label.grid(column=0,row=18,columnspan=5,sticky='W')
#        self.labelVariable17.set(u"Measured PD ")
        
        self.labelVariable24 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable24,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=18,columnspan=5,sticky='W')
        self.labelVariable24.set(u"PD - Left Eye")
        
        self.labelVariable25 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable25,
                              anchor="w",fg="black",bg="white")
        label.grid(column=1,row=18,columnspan=5,sticky='W')
        self.labelVariable25.set(u"PD - Right Eye")
          
        self.labelVariable19 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable19,
                              anchor="w",fg="black",bg="white")
        label.grid(column=2,row=18,columnspan=5,sticky='W')
        self.labelVariable19.set(u"A")
        
        self.labelVariable20 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable20,
                              anchor="w",fg="black",bg="white")
        label.grid(column=3,row=18,columnspan=5,sticky='W')
        self.labelVariable20.set(u"B")
        
        self.labelVariable21 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable21,
                              anchor="w",fg="black",bg="white")
        label.grid(column=4,row=18,columnspan=3,sticky='W')
        self.labelVariable21.set(u"DBL")
        
        self.labelVariable56 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable56,
                              anchor="w",fg="black",bg="white")
        label.grid(column=5,row=18,columnspan=5,sticky='W')
        self.labelVariable56.set(u"FD")

        
        self.labelVariable77 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable77,
                              anchor="w",fg="white",bg="white")
        label.grid(column=5,row=21,columnspan=5,sticky='W')
        self.labelVariable77.set(u"Fasdsdgdgd")


        self.labelVariable48 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable48,
                              anchor="w",fg="white",bg="WHITE")
        label.grid(column=0,row=20,columnspan=5,sticky='W')
        self.labelVariable48.set(u"Spacer after calc")
        
   
         
        self.labelVariable22 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable22,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=24,columnspan=5,sticky='W')
        self.labelVariable22.set(u"For chosen Lens,The Thickness Will be ")   
        
        self.labelVariable78 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable78,
                              anchor="w",fg="white",bg="white")
        label.grid(column=0,row=25,columnspan=5,sticky='W')
        self.labelVariable78.set(u"For chosen ")
        

# Spacer below thickness shown
        self.labelVariable79 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable79,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=27,columnspan=5,sticky='W')
        self.labelVariable79.set(u"     ")
        
#pd- left eye
        self.labelVariable27 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable27,
                              anchor="w",fg="red",bg="white")
        label.grid(column=0,row=19,columnspan=5,sticky='W')
        self.labelVariable27.set(u" ")
#pd-right eye        
        self.labelVariable28 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable28,
                              anchor="w",fg="red",bg="white")
        label.grid(column=1,row=19,columnspan=5,sticky='W')
        self.labelVariable28.set(u" ")
# A param    
        self.labelVariable29 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable29,
                              anchor="w",fg="blue",bg="white")
        label.grid(column=2,row=19,columnspan=5,sticky='W')
        self.labelVariable29.set(u" ")
# B parama        
        self.labelVariable57 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable57,
                              anchor="w",fg="blue",bg="white")
        label.grid(column=3,row=19,columnspan=5,sticky='W')
        self.labelVariable57.set(u" ")
# DBl param      
        self.labelVariable30 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable30,
                              anchor="w",fg="blue",bg="white")
        label.grid(column=4,row=19,columnspan=5,sticky='W')
        self.labelVariable30.set(u" ")
#FD param     
        self.labelVariable31 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable31,
                              anchor="w",fg="black",bg="WHITE")
        label.grid(column=5,row=19,columnspan=5,sticky='W')
        self.labelVariable31.set(u" ")
#L.E. Thickness
        self.labelVariable52 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable52,
                              anchor="w",fg="black",bg="white")
        label.grid(column=1,row=25,columnspan=5,sticky='W')
        self.labelVariable52.set(u"Left Eye")
#R.E. Thickness
        self.labelVariable53 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable53,
                              anchor="w",fg="black",bg="white")
        label.grid(column=3,row=25,columnspan=5,sticky='W')
        self.labelVariable53.set(u"Right Eye")     
#Display L.E. Thickness
        self.labelVariable54 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable54,
                              anchor="w",fg="black",bg="orange")
        label.grid(column=1,row=26,columnspan=5,sticky='W')
        self.labelVariable54.set(u"")       
#Display R.E. Thickness    
        self.labelVariable55 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable55,
                              anchor="w",fg="black",bg="orange")
        label.grid(column=3,row=26,columnspan=5,sticky='W')
        self.labelVariable55.set(u"")
      
        self.labelVariable42 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable42,
                              anchor="w",fg="white",bg="red")
        label.grid(column=0,row=26,columnspan=5,sticky='W')
        self.labelVariable42.set(u"")
        
        #tYPE DISPLAY     
        self.labelVariable47 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable47,
                              anchor="w",fg="white",bg="red")
        label.grid(column=2,row=26,columnspan=5,sticky='W')
        self.labelVariable47.set(u"")
        
        self.labelVariable49 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable49,anchor="e",fg="white",bg="blue")
        label.grid(column=9,row=2,columnspan=1,sticky='W')
        self.labelVariable49.set(u"Comparison Section")
        
       #SPACER  for compare section
#        self.labelVariable63 = Tkinter.StringVar()
#        label = Tkinter.Label(self,textvariable=self.labelVariable63,
#                              anchor="w",fg="WHITE",bg="white", bd = 2)
#        label.grid(column=9,row=12,columnspan=10,sticky='W')
#        self.labelVariable63.set(u"iTitan - A Click Solution for Titan")
        
       #SPACER for compare section
#        self.labelVariable64 = Tkinter.StringVar()
#        label = Tkinter.Label(self,textvariable=self.labelVariable64,
#                              anchor="w",fg="WHITE",bg="white", bd = 2)
#        label.grid(column=8,row=12,columnspan=10,sticky='W')
#        self.labelVariable64.set(u"iTitan - A Click Solution FAJASFK  AFUAOSD")
        
#        self.labelVariable80 = Tkinter.StringVar()
#        label = Tkinter.Label(self,textvariable=self.labelVariable80,
#                              anchor="w",fg="WHITE",bg="white", bd = 20)
#        label.grid(column=9,row=0,columnspan=10,sticky='W')
#        self.labelVariable80.set(u"iTitan - A Click Solution FAJASFK  AFUAOSD")
      #SPACER for compare section  
        self.labelVariable50 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable50,anchor="e",fg="white",bg="white")
        label.grid(column=6,row=10,columnspan=1,sticky='E')
        self.labelVariable50.set(u"Spherical power")
       #SPACER for compare section 
        self.labelVariable51 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable51,anchor="e",fg="white",bg="white")
        label.grid(column=10,row=10,columnspan=1,sticky='E')
        self.labelVariable51.set(u"Spherical power")
        
        self.labelVariable83 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable83,anchor="e",fg="white",bg="white")
        label.grid(column=9,row=1,columnspan=1,sticky='E')
        self.labelVariable83.set(u"Spherical power for spacer")
        
        self.labelVariable84 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable84,anchor="e",fg="white",bg="white")
        label.grid(column=10,row=1,columnspan=1,sticky='E')
        self.labelVariable84.set(u"Spherical power for spacer")
        
        self.labelVariable82 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable82,anchor="e",fg="white",bg="white")
        label.grid(column=12,row=4,columnspan=1,sticky='E')
        self.labelVariable82.set(u"Spherical power for spacer purpose ")
        
        self.labelVariable85 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable85,anchor="e",fg="white",bg="white")
        label.grid(column=8,row=2,columnspan=1,sticky='E')
        self.labelVariable85.set(u"Spherical power for spacer")
        
        self.labelVariable86 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable86,anchor="e",fg="white",bg="white")
        label.grid(column=7,row=31,columnspan=1,sticky='w')
        self.labelVariable86.set(u"Sph")
        
        self.labelVariable61 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable61,anchor="e",fg="blue",bg="white")
        label.grid(column=9,row=4,columnspan=1,sticky='W')
        self.labelVariable61.set(u"Enter the Thickness")
        
      #Comparen Lens 1  
        lst2 = ['CR39 1.498','Crown Glass 1.523','Glass 1.56','Glass 1.7','Glass 1.8','Glass 1.9','Polycarbonate 1.586','Trivex 1.532','Plastics 1.56','Plastics 1.60','Plastics 1.67','Plastics 1.74']
        self.var2 = Tkinter.StringVar()
        self.list2 = Tkinter.OptionMenu(self,self.var2,*lst2)
        self.list2.grid(column=9,row=5,columnspan=6,sticky='W')
      #Comparen Lens 2 
        lst3 = ['CR39 1.498','Crown Glass 1.523','Glass 1.56','Glass 1.7','Glass 1.8','Glass 1.9','Polycarbonate 1.586','Trivex 1.532','Plastics 1.56','Plastics 1.60','Plastics 1.67','Plastics 1.74']
        self.var3 = Tkinter.StringVar()
        self.list3 = Tkinter.OptionMenu(self,self.var3,*lst3)
        self.list3.grid(column=10,row=5,columnspan=6,sticky='W')
      #Comparen Lens 13
        lst4 = ['CR39 1.498','Crown Glass 1.523','Glass 1.56','Glass 1.7','Glass 1.8','Glass 1.9','Polycarbonate 1.586','Trivex 1.532','Plastics 1.56','Plastics 1.60','Plastics 1.67','Plastics 1.74']
        self.var4 = Tkinter.StringVar()
        self.list4 = Tkinter.OptionMenu(self,self.var4,*lst4)
        self.list4.grid(column=11,row=5,columnspan=6,sticky='W')
        
        lst5 = ['ET','CT']
        self.var5 = Tkinter.StringVar()
        self.list5 = Tkinter.OptionMenu(self,self.var5,*lst5)
        self.list5.grid(column=11,row=4,columnspan=6,sticky='W')
#        self.pack_propagate(0)
 #PLOT SEction
        
        self.labelVariable62 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable62,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=7,row=2,columnspan=5,sticky='W')
        self.labelVariable62.set(u"Plot Section")
        
        
        self.labelVariable66 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable66,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=7,row=19,columnspan=5,sticky='W')
        self.labelVariable66.set(u"QR Section")
        
        
        self.grid_columnconfigure(0,weight=1)
        self.pack_propagate(0)
        self.resizable(True,True)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick2(self):
        #self.labelVariable.set( self.entryVariable.get()+" (clicked sumthin else didncha)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

        global udist

        udiste = str(self.var6.get())
        
        
        if udiste=='40 CM':
            udist=0.40
        elif udiste=='50 CM':
            udist=0.50
        elif udiste=='60 CM':
            udist=0.60
        elif udiste=='70 CM':
            udist=0.70
        elif udiste=='80 CM':
            udist=0.80
        elif udiste=='90 CM':
            udist=0.90
            
        def click_and_crop(event, x, y, flags, param):
            global refPt, cropping
            if event == cv2.EVENT_LBUTTONDOWN:
                refPt = [(x, y)]
                cropping = True

            elif event == cv2.EVENT_LBUTTONUP:

                refPt.append((x, y))
                cropping = False
                cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
                cv2.imshow("image", image)
                refPtlist.append(refPt)
 
        image = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        #image = cv2.resize(image, None, fx = 1,fy = 1)
        #image = cv2.imread(args["image"])
        clone = image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", click_and_crop)

        while True:
	# display the image and wait for a keypress
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                image = clone.copy()

	# if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break
     
        for i,refPt in enumerate(refPtlist):
            if len(refPt) == 2:
                roi1 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                #    roi2 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        
#                cv2.imshow("LEFT EYE", roi1)
                #   cv2.imshow("ROI_height", roi2)
                cv2.imwrite("LEFT EYE.jpg", roi1)
       
        boxes = []     
#        def on_mouse(event, x, y, flags, params):
#            if event == cv2.EVENT_LBUTTONDOWN:
#                print 'Mouse Position: '+str(x)+', '+str(y)
#                sbox = [x, y]
#                boxes.append(sbox)

        img = cv2.imread('LEFT EYE.jpg',0)
        img = cv2.medianBlur(img,1)
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,3,80,
#                            param1=60,param2=50,minRadius=0,maxRadius=15)
#
#        circles = np.uint16(np.around(circles))
#        for i in circles[0,:]:
#            # draw the outer circle
#            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#            # draw the center of the circle
#            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),2)
    

    #cv2.imshow('Detected Circle',cimg)
        cv2.imwrite("LEFT PD.jpg",cimg)

        img1=cv2.imread("LEFT PD.jpg")
       #img = cv2.resize(img, None, fx = 1,fy = 1)

        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse)
        cv2.imshow('real image', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    
#        dst_L = math.sqrt(pow(abs(boxes[1][0]-boxes[0][0]),2)+(pow(abs(boxes[1][1]-boxes[0][1]),2)))
#        print dst_L
#        pd1_L=((dst_L*(udist))/1670)
#        pd_L=(math.ceil((pd1_L*1000)*100)/100)

        self.labelVariable27.set(str(pd_L))
        
#        master = Tk()
#
#        msg = Message(master,text = pd_L)
#        msg.config(bg='green', font=('times', 30, 'italic'))
#        msg.pack( )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        clone = image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", click_and_crop)

        while True:
	# display the image and wait for a keypress
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                image = clone.copy()

	# if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break
     
        for i,refPt in enumerate(refPtlist):
            if len(refPt) == 2:
                roi1 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    #       roi2 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
#                cv2.imshow("RIGHT EYE", roi1)
    #       cv2.imshow("ROI_height", roi2)
                cv2.imwrite("RIGHT EYE.jpg", roi1)
       
        boxes = []     
        def on_mouse(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                print 'Mouse Position: '+str(x)+', '+str(y)
                sbox = [x, y]
                boxes.append(sbox)
        
        img = cv2.imread('RIGHT EYE.jpg',0)
        img = cv2.medianBlur(img,1)
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,3,80,
#                            param1=60,param2=50,minRadius=10,maxRadius=20)
#
#        circles = np.uint16(np.around(circles))
#        for i in circles[0,:]:
#            # draw the outer circle
#            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#            # draw the center of the circle
#            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),2)

        cv2.imwrite("RIGHT PD.jpg",cimg)

        img1=cv2.imread("RIGHT PD.jpg")
        #img = cv2.resize(img, None, fx = 1,fy = 1)

        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse)
        cv2.imshow('real image', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        global pd 
        
        dst_R = math.sqrt(pow(abs(boxes[1][0]-boxes[0][0]),2)+(pow(abs(boxes[1][1]-boxes[0][1]),2)))
        print dst_R
        pd1_R=(((dst_R)*(udist))/1670)
        pd_R=(math.ceil((pd1_R*1000)*100)/100)

        self.labelVariable28.set(str(pd_R))
        
        pd=pd_L+pd_R
        pd=(math.ceil(pd*100))/100
        
        print pd
#        master = Tk()
#        msg = Message(master, text = pd)
#        msg.config(bg='red', font=('times', 30, 'bold'))
#        msg.pack( )
      
        
    def OnButtonClick3(self):
#        self.labelVariable4.set( " Frame Measurement Complete ! " )
        global A
        global DBL
        global B
        
        refPt = []
        refPtlist=[]
        cropping = False
        
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        def click_and_crop(event, x, y, flags, param):
            global refPt, cropping
            if event == cv2.EVENT_LBUTTONDOWN:
                refPt = [(x, y)]
                cropping = True

            elif event == cv2.EVENT_LBUTTONUP:

                refPt.append((x, y))
                cropping = False

                cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
                cv2.imshow("image", image)
                refPtlist.append(refPt)
                
#        image = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        src1 = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        src2 = cv2.imread('F:\EYETITAN\PHOTO\Grid.jpg')
        image=(src1+src2)
        
#        image = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        
        #image = cv2.imread(args["image"])
        clone = image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", click_and_crop)

        # keep looping until the 'q' key is pressed
        while True:
            # display the image and wait for a keypress
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF

        	# if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                image = clone.copy()

        	# if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break

            # if there are two reference points, then crop the region of interest
            # from teh image and display it
        

        for i,refPt in enumerate(refPtlist):
            if len(refPt) == 2:
                roi1 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                #    roi2 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                cv2.imshow("ROI"+str(i), roi1)
                #    cv2.imshow("ROI_height", roi2)
                cv2.imwrite("FRAME"+str(i)+".jpg", roi1)
                img1=cv2.imread("FRAME"+str(i)+".jpg")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
        global A
        global DBL
        global B
        global A1
        global B1
        global DBL

        A1 = abs(refPtlist[0][0][1] - refPtlist[0][1][1])
        B1 = abs(refPtlist[0][0][0] - refPtlist[0][1][0])
        DBL1 = abs(refPtlist[1][0][0] - refPtlist[1][1][0])
        B = math.ceil(((A1*udist)/1770)*100*100)/100*10
        
        A = math.ceil(((B1*udist)/1770)*100*100)/100*10
        
        DBL =math.ceil(((DBL1*udist)/1770)*100*100)/100*10
      
        
        print ('DBL=', DBL)
        print ('A=', A)
        print ('B=', B)
        
        self.labelVariable29.set(str(A))
        self.labelVariable57.set(str(B))
        self.labelVariable30.set(str(DBL))
        
        cv2.destroyAllWindows()
        
        global SP_R
        global Name
    
    def OnButtonClick4(self):
        
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
       
        global A,DBL,pd,B,SP_L,CP_L,axis_L,SP_R,CP_R,axis_R,power_R, power_L,RI,decentration,effdia,blanksize,maxthickness_L, maxthickness_R
        
        global minthickness
        
        minthickness=0.0
        
        decentration = float(A+DBL-pd)/2
        SP_L = float(self.entryVariable4.get())
        CP_L = float(self.entryVariable5.get())
        axis_L = float(self.entryVariable6.get())
        
        SP_R = float(self.entryVariable9.get())
        CP_R = float(self.entryVariable10.get())
        axis_R = float(self.entryVariable11.get())
        
#        axis = (float(self.entryVariable6.get()))*(math.pi)/180
        power_L = float((SP_L)+(CP_L)*(math.pow((math.sin(axis_L)),2)))
        
        power_R = float((SP_R)+(CP_R)*(math.pow((math.sin(axis_R)),2)))
        
        SI = str(self.var1.get())
        print str(SI)
        effdia =float(4*(math.pow((decentration+(float(FD))),2)+math.pow((float(B)/2),2)))
        blanksize = float(math.sqrt(effdia))
        if SI== 'CR39 1.498':
            RI=1.498
            minthickness = 2.0
        elif SI== 'Crown Glass 1.523':
            RI=1.523            
            minthickness = 1.5
        elif SI== 'Glass 1.56':
            RI=1.56
            minthickness = 1.8
        elif SI== 'Glass 1.7':
            RI=1.7
            minthickness = 1.7
        elif SI== 'Glass 1.8':
            RI=1.8
            minthickness = 1.6
        elif SI== 'Glass 1.9':
            RI=1.9
            minthickness = 1.5
        elif SI== 'Polycarbonate 1.586':
            RI=1.586
            minthickness = 1.5
        elif SI== 'Trivex 1.532':
            RI=1.532
            minthickness = 1.3
        elif SI== 'Plastics 1.56':
            RI=1.56
            minthickness = 1.71
        elif SI== 'Plastics 1.60':
            RI=1.60
            minthickness = 1.61
        elif SI== 'Plastics 1.67':
            RI=1.67
            minthickness = 1.2
        elif SI== 'Plastics 1.74':
            RI=1.74
            minthickness = 1.4
            
        maxthickness_L = float(minthickness + abs(math.pow((float(blanksize)/2),2)*abs(power_L)/(2000*(RI-1))))
        print maxthickness_L
        
        maxthickness_R = float(minthickness + abs(math.pow((float(blanksize)/2),2)*abs(power_R)/(2000*(RI-1))))
        print maxthickness_R
          
        maxround_L= maxthickness_L-(1000*maxthickness_L-int(1000*maxthickness_L))/1000
        
        maxround_R= maxthickness_R-(1000*maxthickness_R-int(1000*maxthickness_R))/1000
        
        maxround_L = math.ceil( maxround_L*10)/10
        
        maxround_R = math.ceil( maxround_R*10)/10
          
        self.labelVariable54.set(str(maxround_L))
        
        self.labelVariable55.set(str(maxround_R))
        
#        SP_L = float(self.entryVariable4.get())
#        CP_L = float(self.entryVariable5.get())
#        axis_L = (float(self.entryVariable6.get()))
#        
#        SP_R = float(self.entryVariable9.get())
#        CP_R = float(self.entryVariable10.get())
#        axis_R = (float(self.entryVariable11.get()))
        
        if SP_L > 0:
            
            self.labelVariable42.set(u"CT")
                
        else:
            
            self.labelVariable42.set(u"ET")

        if SP_R > 0:
            
            self.labelVariable47.set(u"CT")
            
        else:
            
            self.labelVariable47.set(u"ET")

    def OnButtonClick5(self):
      
        global FD 
        
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        boxes1 = []
        boxes2 = []
        boxes3 = []
        boxes4 = []

        def on_mouse1(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                print 'Mouse Position: '+str(x)+', '+str(y)
                sbox = [x, y]
                boxes1.append(sbox)
        
        def on_mouse2(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                print 'Mouse Position: '+str(x)+', '+str(y)
                sbox = [x, y]
                boxes2.append(sbox)
                
        def on_mouse3(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                print 'Mouse Position: '+str(x)+', '+str(y)
                sbox = [x, y]
                boxes3.append(sbox)
                
        def on_mouse4(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                print 'Mouse Position: '+str(x)+', '+str(y)
                sbox = [x, y]
                boxes4.append(sbox)

        img1 = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        #img = cv2.resize(img, None, fx = 1,fy = 1)
        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse1, 0)
        cv2.imshow('real image', img1)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        dst1 = math.sqrt(pow(abs(boxes1[1][0]-boxes1[0][0]),2)+(pow(abs(boxes1[1][1]-boxes1[0][1]),2)))
        print dst1

        img2 = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        #img = cv2.resize(img, None, fx = 1,fy = 1)
        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse2, 0)
        cv2.imshow('real image', img2)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        dst2 = math.sqrt(pow(abs(boxes2[1][0]-boxes2[0][0]),2)+(pow(abs(boxes2[1][1]-boxes2[0][1]),2)))
        print dst2
        
        img3 = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        #img = cv2.resize(img, None, fx = 1,fy = 1)
        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse3, 0)
        cv2.imshow('real image', img3)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        dst3 = math.sqrt(pow(abs(boxes3[1][0]-boxes3[0][0]),2)+(pow(abs(boxes3[1][1]-boxes3[0][1]),2)))
        print dst3
        
        img4 = cv2.imread('F:\EYETITAN\PHOTO\CUSTOMER.jpg')
        #img = cv2.resize(img, None, fx = 1,fy = 1)
        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse4, 0)
        cv2.imshow('real image', img4)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        dst4 = math.sqrt(pow(abs(boxes4[1][0]-boxes4[0][0]),2)+(pow(abs(boxes4[1][1]-boxes4[0][1]),2)))
        print dst4
        
#       if first number is greater than second number
        
        if dst1 > dst2:
#        //if first number is greater than third number
            if dst1>dst3:
            
#           //if first number is greater than fourth number
                if dst1>dst4:
                    FD_1=dst1
                    print dst1
                else:
#        //fourth number is greater than first number i.e fourth number is also greater than 2nd and 3rd number
                    FD_1=dst4
                    print dst4
                
#        //if 3rd number is greater than 1st number i.e 3rd number is also greater than 2nd number
            else:
            
#        //if 3rd number is greater than 4rth number
                if dst3>dst4:
                    FD_1=dst3
                    print dst3
                else:
#        //if not than 4rth is greatest
                    FD_1=dst4
                    print dst4
        
        
#        //if 2nd is greater than 1st number
        else:
        
            if dst2>dst3:
        
                if dst2>dst4:
                    FD_1=dst2
                    print dst2
                else:
                    FD_1=dst4
                    print dst4 
            else:
        
                if dst3>dst4:
                    FD_1=dst3
                    print dst3
                else:
                    FD_1=dst4
                    print dst4
        

        FD=((FD_1*(udist))/1770)
        print FD*1000
        FD = (math.ceil((FD*1000)*100)/100)
        print FD
        
        self.labelVariable31.set(str(FD))
        
    def OnButtonClick8(self):
       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        self.entryVariable1.set(u" ")
        self.entryVariable2.set(u" ")
        self.entryVariable3.set(u" ")
        self.entryVariable4.set(u" ")
        self.entryVariable5.set(u" ")
        self.entryVariable6.set(u" ")
        self.entryVariable9.set(u" ")
        self.entryVariable10.set(u" ")
        self.entryVariable11.set(u" ")
        self.entryVariable7.set(u" ")
        self.entryVariable8.set(u" ")
        
#        lst1 = [""]
#        self.var1 = Tkinter.StringVar()
#        self.list1 = Tkinter.OptionMenu(self,self.var1,*lst1)
#        self.list1.grid(column=5,row=7,columnspan=10,sticky='W')
        

    def OnButtonClick9(self):
       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        self.labelVariable27.set(u"")
        self.labelVariable28.set(u"")
        self.labelVariable29.set(u"")
        self.labelVariable57.set(u"")
        self.labelVariable30.set(u"")
        self.labelVariable31.set(u"")
        self.labelVariable54.set(u" ")
        self.labelVariable55.set(u" ") 
#        self.labelVariable29.set(u" ")
#        self.labelVariable57.set(u" ")
#        self.labelVariable30.set(u" ")
#        self.labelVariable31.set(u" ")
#     
#        
    def OnButtonClick10(self):
        
        
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        global Name, Age, Gender, pd_L, pd_R,A,DBL,pd,B,SP_L,CP_L,axis_L,SP_R,CP_R,axis_R, RI
        
        Name = str(self.entryVariable1.get())
        
        Age = str(self.entryVariable2.get())
        
        Gender = str(self.entryVariable3.get())
        
        SP_L = str(self.entryVariable4.get())
        CP_L = str(self.entryVariable5.get())
        axis_L = str(self.entryVariable6.get())
        
        SP_R = str(self.entryVariable9.get())
        CP_R = str(self.entryVariable10.get())
        axis_R = str(self.entryVariable11.get())
#        
        RI = str(self.var1.get())
        
        A = str(self.labelVariable29.get())
        B = str(self.labelVariable57.get())
        DBL = str(self.labelVariable30.get())
        FD = str(self.labelVariable31.get())
        
        pd_L=str(self.labelVariable27.get())
        pd_R=str(self.labelVariable28.get())
        
        maxround_L = str(self.labelVariable54.get())
        maxround_R = str(self.labelVariable55.get())
#        
#        FD = FD
#        
       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
# Writing into excel file

        import openpyxl

        xfile = openpyxl.load_workbook('CUSTOMER DETAILS.xlsx')
        
        sheet = xfile.get_sheet_by_name('Custom')
        
        sheet['B3'] = Name
        sheet['B4'] = Age
        sheet['B5'] = Gender
        
        sheet['B9'] = SP_L
        sheet['B10'] = CP_L
        sheet['B11'] = axis_L
  
        sheet['C9'] = SP_R
        sheet['C10'] = CP_R
        sheet['C11'] = axis_R
        
#        sheet['A15'] = pd_L
#        sheet['B15'] = pd_R
        sheet['C15'] = A
        sheet['D15'] = B
        sheet['E15'] = DBL
        sheet['F15'] = FD
        
        sheet['B17'] = maxround_L
        sheet['B18'] = maxround_R
        sheet['A15'] = pd_L
        sheet['B15'] = pd_R

        xfile.save('Customer.xlsx')
        
        bard8 = Image.open("COPYRIGHTS.jpg") 
        bardejov = ImageTk.PhotoImage(bard8)
        labe0 = Label(self, image=bardejov)
        labe0.image = bardejov
        labe0.place(x=980, y=550)
        
        bard9 = Image.open("Titanlogo.jpg") 
        bardejov1 = ImageTk.PhotoImage(bard9)
        labe1 = Label(self, image=bardejov1)
        labe1.image = bardejov1
        labe1.place(x=1100, y=480)
        
    def OnButtonClick11(self):
        
        self.labelVariable84 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable84,
                              anchor="w",fg="black",bg="white", bd = 2)
        label.grid(column=7,row=3,columnspan=5,sticky='W')
        self.labelVariable84.set(u"Diameter is 58mm")
        
        self.labelVariable85 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable85,
                              anchor="w",fg="black",bg="white", bd = 2)
        label.grid(column=7,row=4,columnspan=5,sticky='W')
        self.labelVariable85.set(u"Front Curve is +4.00D")
        
        self.labelVariable86 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable86,
                              anchor="w",fg="black",bg="white", bd = 2)
        label.grid(column=7,row=5,columnspan=5,sticky='W')
        self.labelVariable86.set(u"Asphericity is Paraboloid 0.0p")
        
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        global maxround
        
        if str(self.labelVariable42.get()) == 'ET' :
            
        
            SI = str(self.var1.get())

     
            if SI== 'CR39 1.498':
    #            RI=1.498
    #            minthickness = 2.0
                maxround = float(self.labelVariable54.get())
              #1  
                if 0.0 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 2.0 <= maxround <= 2.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 2.20 <= maxround <= 2.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 2.40 <= maxround <= 2.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  2.60 <= maxround <= 2.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 2.80 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 3.00 <= maxround <= 3.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 3.20 <= maxround <= 3.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 3.40 <= maxround <= 3.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 3.60 <= maxround <= 3.79 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 3.80 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 4.00 <= maxround <= 4.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 4.20 <= maxround <= 4.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #14   
                elif 4.40 <= maxround <= 4.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 4.60 <= maxround <= 4.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 4.80 <= maxround <= 4.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 5.00 <= maxround <= 5.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 5.20 <= maxround <= 5.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\L5.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 5.40 <= maxround <= 5.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 5.60 <= maxround <= 5.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 5.80 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 6.00 <= maxround <= 6.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 6.20 <= maxround <= 6.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 6.40 <= maxround <= 6.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 6.60 <= maxround <= 6.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 6.80 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 7.00 <= maxround <= 7.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 7.20 <= maxround <= 7.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 7.40 <= maxround <= 7.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 7.60 <= maxround <= 7.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif 7.80 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 8.00 <= maxround <= 8.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #33   
                elif 8.20 <= maxround <= 8.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #34   
                elif 8.40 <= maxround <= 8.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.40mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #35    
                elif 8.60 <= maxround <= 8.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #36   
                elif 8.80 <= maxround <= 9.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #37    
                elif 9.20 <= maxround <= 9.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L9.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #38  
                elif 9.50 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L9.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #39   
                elif 10.00 <= maxround <= 10.29:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L10.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #40   
                elif 10.30 <= maxround <= 10.69:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L10.30mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #41  
                elif 10.70 <= maxround <= 10.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L10.70mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #42  
                elif 11.00 <= maxround <= 11.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L11.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #43   
                elif 11.50 <= maxround <= 11.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L11.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #44  
                elif 12.00 <= maxround <= 12.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L12.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #45   
                elif 12.80 <= maxround <= 12.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L12.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                   
                 #45   
                elif 13.00 <=maxround >= 13.49 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L13.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                  #46  
                elif 13.50 <=maxround >= 14.19 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L13.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #47
                elif maxround >= 14.20 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\L14.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
       
            elif SI== 'Trivex 1.532':
                
                RI=1.523            
                minthickness = 1.5
                
                maxround = float(self.labelVariable54.get())
                
                #1  
                if 0.0 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 1.00 <= maxround <= 1.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T1.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 1.25 <= maxround <= 1.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T1.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 1.75 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  2.00 <= maxround <= 2.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 2.25 <= maxround <= 2.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 2.50 <= maxround <= 2.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 2.75 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 3.00 <= maxround <= 3.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 3.25 <= maxround <= 3.49 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 3.50 <= maxround <= 3.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 3.75 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 4.00 <= maxround <= 4.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #14   
                elif 4.25 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 4.50 <= maxround <= 4.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 4.75 <= maxround <= 4.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 5.00 <= maxround <= 5.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 5.25 <= maxround <= 5.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 5.50 <= maxround <= 5.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 5.75 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 6.00 <= maxround <= 6.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T6.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 6.25 <= maxround <= 6.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 6.50 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 6.75 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 7.00 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 7.25 <= maxround <= 7.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 7.50 <= maxround <= 7.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 7.75 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 8.00 <= maxround <= 8.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 8.25 <= maxround <= 8.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif 8.50 <= maxround <= 8.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 8.75 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #33   
                elif 9.00 <= maxround <= 9.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #34   
                elif 9.25 <= maxround <= 9.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #35    
                elif 9.50 <= maxround <= 9.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #36   
                elif 9.75 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #37    
                elif 10.00 <= maxround <= 10.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #38  
                elif 10.25 <= maxround <= 10.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #39   
                elif 10.50 <= maxround <= 10.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #40   
                elif 10.75 <= maxround <= 10.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #41  
                elif 11.00 <= maxround <= 11.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #42  
                elif 11.25 <= maxround <= 11.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #43   
                elif 11.50 <= maxround <= 11.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #44  
                elif 11.75 <= maxround <= 11.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #45   
                elif 12.00 <= maxround <= 12.24 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                   
                 #45   
                elif 12.25 <=maxround >= 12.49 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                  #46  
                elif 12.50 <=maxround >= 12.74 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T13.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #47
                elif maxround >= 12.75 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\T13.20mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                
                      
            elif SI== 'Polycarbonate 1.586':
                
                RI=1.56
                minthickness = 1.8
                
                
                maxround = float(self.labelVariable54.get())
                
                #1
                
                #2  
                if  maxround <= 0.00:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P0.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 0.00 <= maxround <= 0.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P0.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 0.50 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
    
                #5 
                elif  1.00 <= maxround <= 1.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 1.50 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 3.00 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 3.00 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 3.50 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 4.00 <= maxround <= 4.24 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 4.25 <= maxround <= 4.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 4.75 <= maxround <= 5.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 5.50 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #14   
                elif 6.00 <= maxround <= 6.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 6.00 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 6.75 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 7.25 <= maxround <= 7.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P7.50.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 7.50 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 8.00 <= maxround <= 8.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P8.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 8.50 <= maxround <= 8.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P8.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 8.75 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 9.00 <= maxround <= 9.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 9.25 <= maxround <= 9.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.50.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 9.50 <= maxround <= 9.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 9.75 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 10.00 <= maxround <= 10.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 10.25 <= maxround <= 10.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 10.50 <= maxround <= 10.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 10.75 <= maxround <= 10.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 11.00 <= maxround <= 11.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif  11.25 <= maxround <= 11.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 11.50 <= maxround <= 11.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #33   
                elif 11.75 <= maxround <= 11.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #34   
                elif 12.00 <= maxround <= 12.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #35    
                elif 12.25 <= maxround <= 12.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #36   
                elif 12.50 <= maxround <= 12.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #37    
                elif 12.75 <= maxround <= 12.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.00.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #38  
                elif 13.00 <= maxround <= 13.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #39   
                elif 13.25 <= maxround <= 13.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #40   
                elif 13.50 <= maxround <= 13.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #41  
                elif 13.75 <= maxround <= 13.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #42  
                elif 14.00 <= maxround <= 14.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #43   
                elif 14.25 <= maxround <= 14.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #44  
                elif 14.50 <= maxround <= 14.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #45   
                elif 14.75 <= maxround <= 14.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                   
                 #45   
                elif 15.00 <=maxround >= 15.24 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                  #46  
                elif 15.25 <=maxround >= 15.49 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #47
                elif 15.50 >= 15.74 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
    #        
                elif 15.75 >= 15.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P16.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                    
                elif maxround >= 16.30 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\P16.30mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                    
            elif SI== 'Plastics 1.67':
                
                RI=1.67           
                minthickness = 1.2
                
                maxround = float(self.labelVariable54.get())
     
               #-2
                if 0.00 <= maxround <= 0.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S0.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
              #-1  
                if 0.25 <= maxround <= 0.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S0.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                
                #0
                if 0.50 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #1   
                if 1.00 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 1.50 <= maxround <= 1.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S1.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 1.75 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 2.00 <= maxround <= 2.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S2.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  2.50 <= maxround <= 2.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 2.75 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 3.00 <= maxround <= 3.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 3.25 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 3.50 <= maxround <= 3.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 3.75 <= maxround <= 3.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 4.00 <= maxround <= 4.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 4.25 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 4.50 <= maxround <= 4.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #145
                elif 4.75 <= maxround <= 4.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 5.00 <= maxround <= 5.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 5.25 <= maxround <= 5.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 5.50 <= maxround <= 5.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 5.75 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 6.00 <= maxround <= 6.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 6.25 <= maxround <= 6.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 6.50 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 6.75 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 7.00 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 7.25 <= maxround <= 7.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 7.50 <= maxround <= 7.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 7.75 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 8.00 <= maxround <= 8.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 8.25 <= maxround <= 8.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 8.50 <= maxround <= 8.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 8.75 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif 9.00 <= maxround <= 9.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 9.25 <= maxround <= 9.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #33   
                elif 9.50 <= maxround <= 9.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #34   
                elif 9.75 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #35    
                elif 10.00 <= maxround <= 10.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #36   
                elif 10.25 <= maxround <= 10.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #37    
                elif 10.50 <= maxround <= 10.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #38  
                elif 10.75 <= maxround <= 10.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #39   
                elif 11.00 <= maxround <= 11.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #40   
                elif 11.25 <= maxround <= 11.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #41  
                elif 11.50 <= maxround <= 11.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #42  
                elif 11.75 <= maxround <= 11.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #43   
                elif 12.00 <= maxround <= 12.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #44  
                elif 12.25 <= maxround <= 12.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #45   
                elif 12.50 <= maxround <= 12.74 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                   
                 #45   
                elif 12.75 <=maxround >= 12.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S13.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                  #46  
                elif 13.00 <=maxround >= 13.24 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S13.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #47
                elif maxround >= 13.25 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\S13.80mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
           
            elif SI== 'Plastics 1.74':
                
                RI=1.74
                minthickness = 1.4
                
                #-2
                if 0.00 <= maxround <= 0.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C0.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
              #-1  
                if 0.50 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                
                #0
                if 1.00 <= maxround <= 1.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #1   
                if 1.50 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 2.00 <= maxround <= 2.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C2.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 2.25 <= maxround <= 2.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 2.75 <= maxround <= 3.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  3.25 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 3.50 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 4.00 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 4.50 <= maxround <= 4.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 5.00 <= maxround <= 5.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 5.50 <= maxround <= 5.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 6.00 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 6.75 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 7.25 <= maxround <= 7.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #145
                elif 7.75 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 8.00 <= maxround <= 8.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 8.25 <= maxround <= 8.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 8.50 <= maxround <= 8.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 8.75 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 9.00 <= maxround <= 9.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 9.25 <= maxround <= 9.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 9.50 <= maxround <= 9.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 9.75 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 10.00 <= maxround <= 10.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 10.25 <= maxround <= 10.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 10.50 <= maxround <= 10.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 10.75 <= maxround <= 10.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 11.00 <= maxround <= 11.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 11.25 <= maxround <= 11.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 11.50 <= maxround <= 11.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 11.75 <= maxround <= 11.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif 12.00 <= maxround <= 12.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 12.25 <= maxround <= 12.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #33   
                elif 12.50 <= maxround <= 12.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #34   
                elif 12.75 <= maxround <= 12.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #35    
                elif 13.00 <= maxround <= 13.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #36   
                elif 13.25 <= maxround <= 13.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #37    
                elif 13.50 <= maxround <= 13.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #38  
                elif 13.75 <= maxround <= 13.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C14.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #39   
                elif 14.00 <= maxround <= 14.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C14.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #40   
                elif 14.25 <= maxround <= 14.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C14.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #41  
                elif 14.50 <= maxround <= 14.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C15.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #42  
                elif 15.00 <= maxround <= 15.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C15.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #43   
                elif 15.25 <= maxround <= 15.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C15.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #44  
                elif 15.50 <= maxround <= 15.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C16.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
               
                elif 16.00 <=maxround >= 16.49 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C16.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #47
                elif maxround >= 16.50 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C16.60mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                    
        elif str(self.labelVariable42.get()) == 'CT' :    
            
            SI = str(self.var1.get())

     
            if SI== 'CR39 1.498':
    #            RI=1.498
    #            minthickness = 2.0
                maxround = float(self.labelVariable54.get())
              #1  
                if 0.0 <= maxround <= 0.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L0.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 0.50 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L0.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 1.00 <= maxround <= 1.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L0.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 1.50 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  2.00 <= maxround <= 2.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 2.50 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 3.00 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 3.50 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 4.00 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 4.50 <= maxround <= 4.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 5.00 <= maxround <= 5.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 5.25 <= maxround <= 5.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 5.50 <= maxround <= 5.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #14   
                elif 5.75 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 6.00 <= maxround <= 6.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 6.25 <= maxround <= 6.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 6.50 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 6.75 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 7.00 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 7.25 <= maxround <= 7.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 7.50 <= maxround <= 7.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 7.75 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 8.00 <= maxround <= 8.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 8.25 <= maxround <= 8.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 8.50 <= maxround <= 8.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 8.75 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 9.00 <= maxround <= 9.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 9.75 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 10.00 <= maxround <= 10.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L7.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 10.50 <= maxround <= 10.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif 11.00 <= maxround <= 11.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 12.00 <= maxround <= 12.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                    
                #47
                elif maxround >= 13.00 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\L8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
       
            elif SI== 'Trivex 1.532':
                
                RI=1.523            
                minthickness = 1.5
                
                maxround = float(self.labelVariable54.get())
                
                #1  
                if 0.0 <= maxround <= 0.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T0.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 0.50 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T0.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 1.00 <= maxround <= 1.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T0.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 1.50 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  2.00 <= maxround <= 2.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 2.50 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 3.00 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 3.50 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 4.00 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 4.50 <= maxround <= 4.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 5.00 <= maxround <= 5.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 5.25 <= maxround <= 5.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 5.50 <= maxround <= 5.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #14   
                elif 5.75 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 6.00 <= maxround <= 6.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 6.25 <= maxround <= 6.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 6.50 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 6.75 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                
                 #23   
                elif 7.00 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 7.25 <= maxround <= 7.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 7.50 <= maxround <= 7.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 7.75 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 8.00 <= maxround <= 8.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 8.25 <= maxround <= 8.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 8.50 <= maxround <= 8.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 8.75 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif 9.00 <= maxround <= 9.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 9.25 <= maxround <= 9.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #33   
                elif 9.50 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #34   
                elif 10.00 <= maxround <= 10.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #35    
                elif 10.75 <= maxround <= 11.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                
                #47
                elif maxround >= 11.25 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\T8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                
                      
            elif SI== 'Polycarbonate 1.586':
                
                RI=1.56
                minthickness = 1.8
                
                
                maxround = float(self.labelVariable54.get())
                
                #1
                if 0.00 <= maxround <= 0.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P0.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                                
                #2  
                elif  0.50 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P0.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 1.00 <= maxround <= 1.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P0.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 1.50 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
    
                #5 
                elif  2.00 <= maxround <= 2.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 2.50 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 3.00 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 3.50 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 4.00 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 4.50 <= maxround <= 4.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 5.00 <= maxround <= 5.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 5.25 <= maxround <= 5.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 5.50 <= maxround <= 5.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #14   
                elif 5.75 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 6.00 <= maxround <= 6.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 6.25 <= maxround <= 6.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 6.50 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 6.75 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 7.00 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 7.25 <= maxround <= 7.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 7.50 <= maxround <= 7.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 7.75 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 8.00 <= maxround <= 8.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 8.25 <= maxround <= 8.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 8.50 <= maxround <= 8.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 8.75 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 9.00 <= maxround <= 9.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 9.20 <= maxround <= 9.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #30   
                elif 9.40 <= maxround <= 9.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #31   
                elif  9.60 <= maxround <= 9.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #32    
                elif 9.80 <= maxround <= 9.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #33                       
                elif maxround >= 10.00 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\P8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                    
            elif SI== 'Plastics 1.67':
                
                RI=1.67           
                minthickness = 1.2
                
                maxround = float(self.labelVariable54.get())
     
               #-2
                if 0.00 <= maxround <= 0.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S0.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
              #-1  
                if 0.50 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S0.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                
                #0
                if 1.00 <= maxround <= 1.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S0.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #1   
                if 1.50 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 2.00 <= maxround <= 2.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 2.50 <= maxround <= 2.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 3.00 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  3.50 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
            
                #7
                elif 4.00 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 4.50 <= maxround <= 4.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 5.00 <= maxround <= 5.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 5.25 <= maxround <= 5.49 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 5.50 <= maxround <= 5.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 5.75 <= maxround <= 5.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 6.00 <= maxround <= 6.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #145
                elif 6.25 <= maxround <= 6.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 6.50 <= maxround <= 6.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 6.75 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 7.00 <= maxround <= 7.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 7.25 <= maxround <= 7.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 7.50 <= maxround <= 7.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 7.75 <= maxround <= 7.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 8.00 <= maxround <= 8.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 8.20 <= maxround <= 8.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 8.40 <= maxround <= 8.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 8.60 <= maxround <= 8.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 8.80 <= maxround <= 8.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 9.00 <= maxround <= 9.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 9.20 <= maxround <= 9.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 9.40 <= maxround <= 9.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #29    
                elif 9.60 <= maxround <= 9.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
               
                #47
                elif maxround >= 9.80 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\S8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
           
            elif SI== 'Plastics 1.74':
                
                RI=1.74
                minthickness = 1.4
                
                #-2
                if 0.00 <= maxround <= 0.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C0.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
              #-1  
                if 0.20 <= maxround <= 0.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C0.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                                
                #0
                elif 0.40 <= maxround <= 0.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C0.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #1   
                elif 0.60 <= maxround <= 0.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #2
                elif 0.80 <= maxround <= 0.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #3
                elif 1.00 <= maxround <= 1.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #4
                elif 1.25 <= maxround <= 1.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #5 
                elif  1.50 <= maxround <= 1.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #6
                elif 1.75 <= maxround <= 1.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #7
                elif 2.00 <= maxround <= 2.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #8
                elif 2.25 <= maxround <= 2.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #9    
                elif 2.50 <= maxround <= 2.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #10    
                elif 2.75 <= maxround <= 2.99 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #11  
                elif 3.00 <= maxround <= 3.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #12   
                elif 3.25 <= maxround <= 3.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #13  
                elif 3.50 <= maxround <= 3.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #145
                elif 3.75 <= maxround <= 3.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #15   
                elif 4.00 <= maxround <= 4.24:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #16  
                elif 4.25 <= maxround <= 4.49:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #17  
                elif 4.50 <= maxround <= 4.74:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C5.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #18   
                elif 4.75 <= maxround <= 4.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\ET\C5.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #19   
                elif 5.00 <= maxround <= 5.09:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C5.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #20   
                elif 5.10 <= maxround <= 5.19:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C5.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #21   
                elif 5.20 <= maxround <= 5.29:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #22   
                elif 5.30 <= maxround <= 5.39:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #23   
                elif 5.40 <= maxround <= 5.59:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #24   
                elif 5.60 <= maxround <= 5.69:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #25   
                elif 5.70 <= maxround <= 5.89:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #26   
                elif 5.90 <= maxround <= 6.29:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.25mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #27   
                elif 6.30 <= maxround <= 6.79:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.50mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                 #28   
                elif 6.80 <= maxround <= 6.99:
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.75mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                #47
                elif maxround >= 7.00 :
                    ima = cv2.imread('C:\Users\Guest1\Desktop\CT\C8.00mm.jpg')
                    cv2.imwrite("thick.jpg",ima)
                    
                    
        bard1 = Image.open("thick.jpg") 
        bardejov = ImageTk.PhotoImage(bard1)
        label0 = Label(self, image=bardejov)
        label0.image = bardejov
        label0.place(x=650, y=180)
#        
#        rot = Image.open("F:\EYETITAN\CODES\NON -EDITABLE CODES\UI on 24.05.2016\dsp1.jpg") 
#        rotunda = ImageTk.PhotoImage(rot)
#        label2 = Label(self, image=rotunda)
#        label2.image = rotunda
#        label2.place(x=720, y=410)        
#              
#        minc = Image.open("F:\EYETITAN\CODES\NON -EDITABLE CODES\UI on 24.05.2016\dsp2.jpg") 
#        mincol = ImageTk.PhotoImage(minc)
#        label3 = Label(self, image=mincol)
#        label3.image = mincol      
#        label3.place(x=830, y=410) 
#        thick = cv2.imread('F:\\EYETITAN\CODES\\NON -EDITABLE CODES\\UI on 24.05.2016\\thick.jpg')
#        cv2.imshow('thick1',thick)
#        cv2.waitkey()   
#        img = Image.open('thick.jpg')
#        img.show() 
        
    def OnButtonClick6(self):
       
 
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
            
        qr = pyqrcode.create(
                             str('Customer Details')+str(':')+str('\n')+
                             str('Name')+str('-')+str(self.entryVariable1.get())+str('\n')+
                             str('Age')+str('-')+str(self.entryVariable2.get())+str('\n')+
                             str('Gender')+str('-')+str(self.entryVariable3.get())+str('\n')+
                             
                             str('Left Eye')+str(':')+str('\n')+
                             str('SP')+str('-')+str(self.entryVariable4.get())+str('\n')+
                             str('CP')+str('-')+str(self.entryVariable5.get())+str('\n')+
                             str('AXIS')+str('-')+str(self.entryVariable6.get())+str('\n')+
                             
                             str('Right Eye')+str(':')+str('\n')+
                             str('SP')+str('-')+str(self.entryVariable9.get())+str('\n')+
                             str('CP')+str('-')+str(self.entryVariable10.get())+str('\n')+
                             str('AXIS')+str('-')+str(self.entryVariable11.get())+str('\n')+
#                             
                             str('Calculated Parameters')+str(':')+str('\n')+
                             str('PD (L.E)')+str('-')+str(self.labelVariable27.get())+str('\n')+
                             str('PD (R.E)')+str('-')+str(self.labelVariable28.get())+str('\n')+
#                             
                             str('A')+str('-')+str(self.labelVariable29.get())+str('\n')+
                             str('B')+str('-')+str(self.labelVariable57.get())+str('\n')+
                             str('DBL')+str('-')+str(self.labelVariable30.get())+str('\n')+
                             str('FD')+str('-')+str(self.labelVariable31.get())+str('\n')+
                             
                             str('Calculated Thickness')+str(':')+str('\n')+
                             str('Left Eye')+str('-')+str(self.labelVariable54.get())+str('\n')+
                             str('Right Eye')+str('-')+str(self.labelVariable55.get())+str('\n'))
                          
                            
                                                     
        qr.png('code.png', scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
#        qr.show()
        
        bard5 = Image.open("code.png") 
        bardejov = ImageTk.PhotoImage(bard5)
        labe0 = Label(self, image=bardejov)
        labe0.image = bardejov
        labe0.place(x=570, y=490)
        
        bard6 = Image.open("INFO.jpg") 
        bardejov = ImageTk.PhotoImage(bard6)
        labe0 = Label(self, image=bardejov)
        labe0.image = bardejov
        labe0.place(x=780, y=550)
        
        bard7 = Image.open("COPYRIGHTS.jpg") 
        bardejov = ImageTk.PhotoImage(bard7)
        labe0 = Label(self, image=bardejov)
        labe0.image = bardejov
        labe0.place(x=980, y=550)
        
        bard9 = Image.open("Titanlogo.jpg") 
        bardejov1 = ImageTk.PhotoImage(bard9)
        labe1 = Label(self, image=bardejov1)
        labe1.image = bardejov1
        labe1.place(x=1100, y=480)
    
#    def OnButtonClick12(self):
#        
#        d = 2.2
#        e = 4.9
#        self.labelVariable54.set(d)
#        
#        self.labelVariable55.set(e)
#        
#    def OnButtonClick13(self):
#        
#        d = 4.3
#        e = 4.5
#        self.labelVariable54.set(d)
#        
#        self.labelVariable55.set(e)
#        
#    def OnButtonClick14(self):
#        
#        d = 6.1
#        e = 4.5
#        self.labelVariable54.set(d)
#        
#        self.labelVariable55.set(e)
#        
#    def OnButtonClick15(self):
#        
#        d = 8.3
#        e = 4.0
#        self.labelVariable54.set(d)
#        
#        self.labelVariable55.set(e)
#        
    def OnButtonClick16(self):
        

        val1 = {}
        
        typ=[]
        
        typ = str(self.var5.get())
        
        val1['drp0'] = str(self.var2.get())
        
        val1['drp1']= str(self.var3.get())
        
        val1['drp2'] = str(self.var4.get())
        
        thickplot = float(self.entryVariable12.get())
        
        
        if typ == 'ET':
            
            image = {}
            val1 = {}
        
            typ=[]
        
            typ = str(self.var5.get())
            
            val1['drp0'] = str(self.var2.get())
            
            val1['drp1']= str(self.var3.get())
            
            val1['drp2'] = str(self.var4.get())
            
            thickplot = float(self.entryVariable12.get())
            
            for i in range(0,3) :

                if val1['drp' + str(i)]=='CR39 1.498':
                    
                    print 'Suganth'
              #1  
                    if 0.0 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)]) 
#                        
                    #2
                    elif 2.0 <= thickplot <= 2.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
#                        
                    #3
                    elif 2.20 <= thickplot <= 2.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
#                        
                    #4
                    elif 2.40 <= thickplot <= 2.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
#                        
                    #5 
                    elif  2.60 <= thickplot <= 2.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
#                        
                    #6
                    elif 2.80 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L2.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
#                        
                    #7
                    elif 3.00 <= thickplot <= 3.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)]) 
#                        
                    #8
                    elif 3.20 <= thickplot <= 3.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 3.40 <= thickplot <= 3.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 3.60 <= thickplot <= 3.79 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 3.80 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L3.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 4.00 <= thickplot <= 4.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 4.20 <= thickplot <= 4.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #14   
                    elif 4.40 <= thickplot <= 4.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 4.60 <= thickplot <= 4.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 4.80 <= thickplot <= 4.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L4.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 5.00 <= thickplot <= 5.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 5.20 <= thickplot <= 5.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\L5.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 5.40 <= thickplot <= 5.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 5.60 <= thickplot <= 5.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #21   
                    elif 5.80 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L5.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 6.00 <= thickplot <= 6.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 6.20 <= thickplot <= 6.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 6.40 <= thickplot <= 6.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                     #25   
                    elif 6.60 <= thickplot <= 6.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 6.80 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L6.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 7.00 <= thickplot <= 7.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 7.20 <= thickplot <= 7.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 7.40 <= thickplot <= 7.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #30   
                    elif 7.60 <= thickplot <= 7.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #31   
                    elif 7.80 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L7.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #32    
                    elif 8.00 <= thickplot <= 8.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #33   
                    elif 8.20 <= thickplot <= 8.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #34   
                    elif 8.40 <= thickplot <= 8.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.40mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #35    
                    elif 8.60 <= thickplot <= 8.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #36   
                    elif 8.80 <= thickplot <= 9.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L8.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #37    
                    elif 9.20 <= thickplot <= 9.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L9.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #38  
                    elif 9.50 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L9.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #39   
                    elif 10.00 <= thickplot <= 10.29:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L10.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #40   
                    elif 10.30 <= thickplot <= 10.69:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L10.30mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #41  
                    elif 10.70 <= thickplot <= 10.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L10.70mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #42  
                    elif 11.00 <= thickplot <= 11.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L11.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #43   
                    elif 11.50 <= thickplot <= 11.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L11.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #44  
                    elif 12.00 <= thickplot <= 12.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L12.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #45   
                    elif 12.80 <= thickplot <= 12.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L12.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                       
                     #45   
                    elif 13.00 <=thickplot >= 13.49 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L13.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                      #46  
                    elif 13.50 <=thickplot >= 14.19 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L13.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #47
                    elif thickplot >= 14.20 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\L14.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
           
                elif val1['drp' + str(i)]== 'Trivex 1.532':
                    
               
                    thickplot = float(self.entryVariable12.get())
                    
                    
                    #1  
                    if 0.0 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T1.00mm.jpg')              
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                    #2
                    elif 1.00 <= thickplot <= 1.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T1.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 1.25 <= thickplot <= 1.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T1.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 1.75 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #5 
                    elif  2.00 <= thickplot <= 2.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #6
                    elif 2.25 <= thickplot <= 2.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #7
                    elif 2.50 <= thickplot <= 2.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 2.75 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 3.00 <= thickplot <= 3.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 3.25 <= thickplot <= 3.49 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 3.50 <= thickplot <= 3.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T3.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 3.75 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 4.00 <= thickplot <= 4.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #14   
                    elif 4.25 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 4.50 <= thickplot <= 4.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 4.75 <= thickplot <= 4.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 5.00 <= thickplot <= 5.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 5.25 <= thickplot <= 5.49:
                        
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 5.50 <= thickplot <= 5.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T5.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 5.75 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #21   
                    elif 6.00 <= thickplot <= 6.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T6.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 6.25 <= thickplot <= 6.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 6.50 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 6.75 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 7.00 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 7.25 <= thickplot <= 7.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 7.50 <= thickplot <= 7.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 7.75 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 8.00 <= thickplot <= 8.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #30   
                    elif 8.25 <= thickplot <= 8.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T8.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #31   
                    elif 8.50 <= thickplot <= 8.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)]) 
                        
                    #32    
                    elif 8.75 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #33   
                    elif 9.00 <= thickplot <= 9.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #34   
                    elif 9.25 <= thickplot <= 9.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T9.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #35    
                    elif 9.50 <= thickplot <= 9.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #36   
                    elif 9.75 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #37    
                    elif 10.00 <= thickplot <= 10.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #38  
                    elif 10.25 <= thickplot <= 10.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T10.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #39   
                    elif 10.50 <= thickplot <= 10.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #40   
                    elif 10.75 <= thickplot <= 10.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #41  
                    elif 11.00 <= thickplot <= 11.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #42  
                    elif 11.25 <= thickplot <= 11.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T11.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #43   
                    elif 11.50 <= thickplot <= 11.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #44  
                    elif 11.75 <= thickplot <= 11.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #45   
                    elif 12.00 <= thickplot <= 12.24 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                       
                     #45   
                    elif 12.25 <=thickplot >= 12.49 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T12.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                      #46  
                    elif 12.50 <=thickplot >= 12.74 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T13.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #47
                    elif thickplot >= 12.75 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\T13.20mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                         
                elif val1['drp' + str(i)]== 'Polycarbonate 1.586':
                    
                    thickplot = float(self.entryVariable12.get())
                    

                    #2  
                    if  thickplot <= 0.00:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P0.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 0.00 <= thickplot <= 0.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P0.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 0.50 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
        
                    #5 
                    elif  1.00 <= thickplot <= 1.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #6
                    elif 1.50 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #7
                    elif 3.00 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 3.00 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 3.50 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 4.00 <= thickplot <= 4.24 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 4.25 <= thickplot <= 4.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 4.75 <= thickplot <= 5.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 5.50 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #14   
                    elif 6.00 <= thickplot <= 6.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 6.00 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 6.75 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 7.25 <= thickplot <= 7.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P7.50.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 7.50 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 8.00 <= thickplot <= 8.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P8.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 8.50 <= thickplot <= 8.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P8.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #21   
                    elif 8.75 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 9.00 <= thickplot <= 9.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 9.25 <= thickplot <= 9.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.50.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 9.50 <= thickplot <= 9.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P9.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 9.75 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 10.00 <= thickplot <= 10.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 10.25 <= thickplot <= 10.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 10.50 <= thickplot <= 10.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P10.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 10.75 <= thickplot <= 10.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #30   
                    elif 11.00 <= thickplot <= 11.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #31   
                    elif  11.25 <= thickplot <= 11.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #32    
                    elif 11.50 <= thickplot <= 11.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P11.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #33   
                    elif 11.75 <= thickplot <= 11.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #34   
                    elif 12.00 <= thickplot <= 12.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #35    
                    elif 12.25 <= thickplot <= 12.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #36   
                    elif 12.50 <= thickplot <= 12.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P12.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #37    
                    elif 12.75 <= thickplot <= 12.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.00.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #38  
                    elif 13.00 <= thickplot <= 13.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #39   
                    elif 13.25 <= thickplot <= 13.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #40   
                    elif 13.50 <= thickplot <= 13.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P13.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #41  
                    elif 13.75 <= thickplot <= 13.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #42  
                    elif 14.00 <= thickplot <= 14.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #43   
                    elif 14.25 <= thickplot <= 14.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #44  
                    elif 14.50 <= thickplot <= 14.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P14.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #45   
                    elif 14.75 <= thickplot <= 14.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                       
                     #45   
                    elif 15.00 <=thickplot >= 15.24 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                      #46  
                    elif 15.25 <=thickplot >= 15.49 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #47
                    elif 15.50 >= 15.74 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P15.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
        #        
                    elif 15.75 >= 15.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P16.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                        
                    elif thickplot >= 16.30 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\P16.30mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                        
                elif val1['drp' + str(i)]== 'Plastics 1.67':
                    
                    
                    
                    thickplot = float(self.entryVariable12.get())

         
                   #-2
                    if 0.00 <= thickplot <= 0.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S0.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                  #-1  
                    elif 0.25 <= thickplot <= 0.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S0.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                    
                    #0
                    elif 0.50 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #1   
                    elif 1.00 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #2
                    elif 1.50 <= thickplot <= 1.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S1.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 1.75 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 2.00 <= thickplot <= 2.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S2.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #5 
                    elif  2.50 <= thickplot <= 2.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #6
                    elif 2.75 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #7
                    elif 3.00 <= thickplot <= 3.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 3.25 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 3.50 <= thickplot <= 3.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S3.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 3.75 <= thickplot <= 3.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 4.00 <= thickplot <= 4.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 4.25 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 4.50 <= thickplot <= 4.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #145
                    elif 4.75 <= thickplot <= 4.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 5.00 <= thickplot <= 5.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 5.25 <= thickplot <= 5.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 5.50 <= thickplot <= 5.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S5.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 5.75 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 6.00 <= thickplot <= 6.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 6.25 <= thickplot <= 6.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #21   
                    elif 6.50 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 6.75 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 7.00 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 7.25 <= thickplot <= 7.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 7.50 <= thickplot <= 7.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 7.75 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 8.00 <= thickplot <= 8.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.25mm.jpg')                       
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 8.25 <= thickplot <= 8.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 8.50 <= thickplot <= 8.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S8.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #30   
                    elif 8.75 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #31   
                    elif 9.00 <= thickplot <= 9.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #32    
                    elif 9.25 <= thickplot <= 9.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #33   
                    elif 9.50 <= thickplot <= 9.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S9.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #34   
                    elif 9.75 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #35    
                    elif 10.00 <= thickplot <= 10.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.25mm.jpg')                        
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #36   
                    elif 10.25 <= thickplot <= 10.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #37    
                    elif 10.50 <= thickplot <= 10.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S10.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #38  
                    elif 10.75 <= thickplot <= 10.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #39   
                    elif 11.00 <= thickplot <= 11.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #40   
                    elif 11.25 <= thickplot <= 11.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #41  
                    elif 11.50 <= thickplot <= 11.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S11.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #42  
                    elif 11.75 <= thickplot <= 11.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #43   
                    elif 12.00 <= thickplot <= 12.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #44  
                    elif 12.25 <= thickplot <= 12.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #45   
                    elif 12.50 <= thickplot <= 12.74 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S12.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                       
                     #45   
                    elif 12.75 <=thickplot >= 12.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S13.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                      #46  
                    elif 13.00 <=thickplot >= 13.24 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S13.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #47
                    elif thickplot >= 13.25 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\S13.80mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
               
                elif val1['drp' + str(i)]== 'Plastics 1.74':
                    
                   
                    thickplot = float(self.entryVariable12.get())
                    
                    #-2
                    if 0.00 <= thickplot <= 0.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C0.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                  #-1  
                    if 0.50 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                    
                    #0
                    if 1.00 <= thickplot <= 1.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #1   
                    if 1.50 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #2
                    elif 2.00 <= thickplot <= 2.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C2.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 2.25 <= thickplot <= 2.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 2.75 <= thickplot <= 3.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #5 
                    elif  3.25 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #6
                    elif 3.50 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #7
                    elif 4.00 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 4.50 <= thickplot <= 4.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 5.00 <= thickplot <= 5.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 5.50 <= thickplot <= 5.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 6.00 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 6.75 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 7.25 <= thickplot <= 7.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #145
                    elif 7.75 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 8.00 <= thickplot <= 8.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 8.25 <= thickplot <= 8.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 8.50 <= thickplot <= 8.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C8.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 8.75 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 9.00 <= thickplot <= 9.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 9.25 <= thickplot <= 9.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #21   
                    elif 9.50 <= thickplot <= 9.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C9.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 9.75 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 10.00 <= thickplot <= 10.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 10.25 <= thickplot <= 10.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 10.50 <= thickplot <= 10.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C10.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 10.75 <= thickplot <= 10.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 11.00 <= thickplot <= 11.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 11.25 <= thickplot <= 11.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 11.50 <= thickplot <= 11.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C11.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #30   
                    elif 11.75 <= thickplot <= 11.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #31   
                    elif 12.00 <= thickplot <= 12.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #32    
                    elif 12.25 <= thickplot <= 12.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #33   
                    elif 12.50 <= thickplot <= 12.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C12.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #34   
                    elif 12.75 <= thickplot <= 12.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #35    
                    elif 13.00 <= thickplot <= 13.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #36   
                    elif 13.25 <= thickplot <= 13.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #37    
                    elif 13.50 <= thickplot <= 13.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C13.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #38  
                    elif 13.75 <= thickplot <= 13.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C14.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #39   
                    elif 14.00 <= thickplot <= 14.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C14.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #40   
                    elif 14.25 <= thickplot <= 14.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C14.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #41  
                    elif 14.50 <= thickplot <= 14.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C15.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #42  
                    elif 15.00 <= thickplot <= 15.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C15.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #43   
                    elif 15.25 <= thickplot <= 15.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C15.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #44  
                    elif 15.50 <= thickplot <= 15.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C16.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                   
                    elif 16.00 <=thickplot >= 16.49 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C16.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #47
                    elif thickplot >= 16.50 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C16.60mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                        
        if typ == 'CT':
            
            
            image = {}
            
            val1 = {}
        
            typ=[]
            
            typ = str(self.var5.get())
            
            val1['drp0'] = str(self.var2.get())
            
            val1['drp1']= str(self.var3.get())
            
            val1['drp2'] = str(self.var4.get())
            
            thickplot = float(self.entryVariable12.get())
            
            for i in range(0,3):
            
                if val1['drp' + str(i)] == 'CR39 1.498':
        
                     #1 
                    if 0.0 <= thickplot <= 0.49:
                        
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L0.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #2
                    elif 0.50 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L0.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                        #3
                    elif 1.00 <= thickplot <= 1.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L0.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                            
                        #4
                    elif 1.50 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                        #5 
                    elif  2.00 <= thickplot <= 2.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #6
                    elif 2.50 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #7
                    elif 3.00 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L1.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                        #8
                    elif 3.50 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #9    
                    elif 4.00 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #10    
                    elif 4.50 <= thickplot <= 4.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #11  
                    elif 5.00 <= thickplot <= 5.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #12   
                    elif 5.25 <= thickplot <= 5.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                        #13  
                    elif 5.50 <= thickplot <= 5.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                         #14   
                    elif 5.75 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                         #15   
                    elif 6.00 <= thickplot <= 6.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L3.75mm.jpg')
                            
                            
                         #16  
                    elif 6.25 <= thickplot <= 6.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                         #17  
                    elif 6.50 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                         #18   
                    elif 6.75 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #19   
                    elif 7.00 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                         #20   
                    elif 7.25 <= thickplot <= 7.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #21   
                    elif 7.50 <= thickplot <= 7.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #22   
                    elif 7.75 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #23   
                    elif 8.00 <= thickplot <= 8.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L5.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #24   
                    elif 8.25 <= thickplot <= 8.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #25   
                    elif 8.50 <= thickplot <= 8.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #26   
                    elif 8.75 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                         #27   
                    elif 9.00 <= thickplot <= 9.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])   
                            
                         #28   
                    elif 9.75 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #29    
                    elif 10.00 <= thickplot <= 10.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L7.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #30   
                    elif 10.50 <= thickplot <= 10.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #31   
                    elif 11.00 <= thickplot <= 11.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #32    
                    elif 12.00 <= thickplot <= 12.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])    
                            
                        #47
                    elif thickplot >= 13.00 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\L8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
           
                elif val1['drp' + str(i)] == 'Trivex 1.532':
                    
                    RI=1.523            
                    minthickness = 1.5
     
                             
                    if 0.0 <= thickplot <= 0.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T0.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #2
                    elif 0.50 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T0.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 1.00 <= thickplot <= 1.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T0.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 1.50 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #5 
                    elif  2.00 <= thickplot <= 2.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #6
                    elif 2.50 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #7
                    elif 3.00 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T1.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 3.50 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 4.00 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 4.50 <= thickplot <= 4.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 5.00 <= thickplot <= 5.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 5.25 <= thickplot <= 5.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 5.50 <= thickplot <= 5.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #14   
                    elif 5.75 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 6.00 <= thickplot <= 6.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T3.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 6.25 <= thickplot <= 6.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 6.50 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 6.75 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    
                     #23   
                    elif 7.00 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 7.25 <= thickplot <= 7.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 7.50 <= thickplot <= 7.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 7.75 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 8.00 <= thickplot <= 8.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T5.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 8.25 <= thickplot <= 8.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 8.50 <= thickplot <= 8.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #30   
                    elif 8.75 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #31   
                    elif 9.00 <= thickplot <= 9.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #32    
                    elif 9.25 <= thickplot <= 9.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #33   
                    elif 9.50 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #34   
                    elif 10.00 <= thickplot <= 10.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #35    
                    elif 10.75 <= thickplot <= 11.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    
                    #47
                    elif thickplot >= 11.25 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\T8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    
                          
                elif val1['drp' + str(i)]== 'Polycarbonate 1.586':
                    
                    RI=1.56
                    minthickness = 1.8
     
#                            thickplot = str(self.entryVariable1.get())
#                            thickplot = float(thickplot)
                    
                    #1
                    if 0.00 <= thickplot <= 0.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P0.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                                    
                    #2  
                    elif  0.50 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P0.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 1.00 <= thickplot <= 1.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P0.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 1.50 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
        
                    #5 
                    elif  2.00 <= thickplot <= 2.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #6
                    elif 2.50 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #7
                    elif 3.00 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P1.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 3.50 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 4.00 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 4.50 <= thickplot <= 4.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 5.00 <= thickplot <= 5.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 5.25 <= thickplot <= 5.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 5.50 <= thickplot <= 5.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #14   
                    elif 5.75 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 6.00 <= thickplot <= 6.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P3.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 6.25 <= thickplot <= 6.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 6.50 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 6.75 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 7.00 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 7.25 <= thickplot <= 7.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 7.50 <= thickplot <= 7.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 7.75 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 8.00 <= thickplot <= 8.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P5.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 8.25 <= thickplot <= 8.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 8.50 <= thickplot <= 8.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 8.75 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 9.00 <= thickplot <= 9.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 9.20 <= thickplot <= 9.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #30   
                    elif 9.40 <= thickplot <= 9.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #31   
                    elif  9.60 <= thickplot <= 9.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #32    
                    elif 9.80 <= thickplot <= 9.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #33                       
                    elif thickplot >= 10.00 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\P8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                        
                elif val1['drp' + str(i)]== 'Plastics 1.67':
                    
                    RI=1.67           
                    minthickness = 1.2
#                    
#                    thickplot = str(self.entryVariable1.get())
#                             thickplot = float(thickplot)
         
                   #-2
                    if 0.00 <= thickplot <= 0.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S0.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                  #-1  
                    if 0.50 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S0.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                    
                    #0
                    if 1.00 <= thickplot <= 1.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S0.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #1   
                    if 1.50 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #2
                    elif 2.00 <= thickplot <= 2.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 2.50 <= thickplot <= 2.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 3.00 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S1.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #5 
                    elif  3.50 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                
                    #7
                    elif 4.00 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 4.50 <= thickplot <= 4.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 5.00 <= thickplot <= 5.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 5.25 <= thickplot <= 5.49 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 5.50 <= thickplot <= 5.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 5.75 <= thickplot <= 5.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])         
                        
                    #13  
                    elif 6.00 <= thickplot <= 6.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S3.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #145
                    elif 6.25 <= thickplot <= 6.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 6.50 <= thickplot <= 6.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 6.75 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 7.00 <= thickplot <= 7.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 7.25 <= thickplot <= 7.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 7.50 <= thickplot <= 7.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 7.75 <= thickplot <= 7.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #21   
                    elif 8.00 <= thickplot <= 8.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S5.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 8.20 <= thickplot <= 8.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 8.40 <= thickplot <= 8.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 8.60 <= thickplot <= 8.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 8.80 <= thickplot <= 8.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 9.00 <= thickplot <= 9.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 9.20 <= thickplot <= 9.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 9.40 <= thickplot <= 9.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #29    
                    elif 9.60 <= thickplot <= 9.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                   
                    #47
                    elif thickplot >= 9.80 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\S8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
               
                elif val1['drp' + str(i)]== 'Plastics 1.74':
                    
                    RI=1.74
                    minthickness = 1.4
                    
#                             thickplot = str(self.entryVariable1.get())
#                             thickplot = float(thickplot)                    
     #-2
                    if 0.00 <= thickplot <= 0.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C0.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                  #-1  
                    if 0.20 <= thickplot <= 0.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C0.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                                    
                    #0
                    elif 0.40 <= thickplot <= 0.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C0.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #1   
                    elif 0.60 <= thickplot <= 0.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #2
                    elif 0.80 <= thickplot <= 0.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #3
                    elif 1.00 <= thickplot <= 1.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #4
                    elif 1.25 <= thickplot <= 1.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C1.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #5 
                    elif  1.50 <= thickplot <= 1.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #6
                    elif 1.75 <= thickplot <= 1.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #7
                    elif 2.00 <= thickplot <= 2.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #8
                    elif 2.25 <= thickplot <= 2.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C2.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #9    
                    elif 2.50 <= thickplot <= 2.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #10    
                    elif 2.75 <= thickplot <= 2.99 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #11  
                    elif 3.00 <= thickplot <= 3.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #12   
                    elif 3.25 <= thickplot <= 3.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C3.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #13  
                    elif 3.50 <= thickplot <= 3.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #145
                    elif 3.75 <= thickplot <= 3.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #15   
                    elif 4.00 <= thickplot <= 4.24:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #16  
                    elif 4.25 <= thickplot <= 4.49:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C4.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #17  
                    elif 4.50 <= thickplot <= 4.74:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C5.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #18   
                    elif 4.75 <= thickplot <= 4.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\ET\C5.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #19   
                    elif 5.00 <= thickplot <= 5.09:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C5.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #20   
                    elif 5.10 <= thickplot <= 5.19:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C5.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #21   
                    elif 5.20 <= thickplot <= 5.29:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #22   
                    elif 5.30 <= thickplot <= 5.39:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #23   
                    elif 5.40 <= thickplot <= 5.59:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #24   
                    elif 5.60 <= thickplot <= 5.69:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C6.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #25   
                    elif 5.70 <= thickplot <= 5.89:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #26   
                    elif 5.90 <= thickplot <= 6.29:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.25mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #27   
                    elif 6.30 <= thickplot <= 6.79:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.50mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                     #28   
                    elif 6.80 <= thickplot <= 6.99:
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C7.75mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])
                        
                    #47
                    elif thickplot >= 7.00 :
                        image['dsp' + str(i)] = cv2.imread('C:\Users\Guest1\Desktop\CT\C8.00mm.jpg')
                        cv2.imwrite("dsp"+str(i)+".jpg",image['dsp' + str(i)])

        bard = Image.open("F:\EYETITAN\CODES\NON -EDITABLE CODES\UI on 24.05.2016\dsp0.jpg") 
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=900, y=170)
          
        rot = Image.open("F:\EYETITAN\CODES\NON -EDITABLE CODES\UI on 24.05.2016\dsp1.jpg") 
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=1050, y=170)        
              
        minc = Image.open("F:\EYETITAN\CODES\NON -EDITABLE CODES\UI on 24.05.2016\dsp2.jpg") 
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol      
        label3.place(x=1200, y=170)             
   
   
    def OnButtonClick12(self):
       
 
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
        minc0 = Image.open("CLEANER.jpg") 
        mincol0 = ImageTk.PhotoImage(minc0)
        label3 = Label(self, image=mincol0)
        label3.image = mincol0     
        label3.place(x=900, y=175)

    
if __name__ == "__main__":  
    
    app = simpleapp_tk(None) 
    
    app.title('iTitan')
    app.mainloop()