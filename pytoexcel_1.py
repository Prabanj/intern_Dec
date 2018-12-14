# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 22:43:50 2018

@author: Administrator
"""

import serial

from openpyxl import Workbook


ser = serial.Serial()
ser.port = 'COM16'
ser.open()

wb = Workbook()

dest_filename = 'Data_log.xlsx'

ws1 = wb.active

ws2 = wb.create_sheet(title="Dec")

for i in range(3,100):
    
    a = ser.readline()
    
    a = (int(a[6:18]))
    
    print(a)
    
    B = str('B'+str(i))

    ws2[B] = a

    wb.save(filename = dest_filename)