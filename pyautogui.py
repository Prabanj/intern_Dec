import pyautogui 
import serial
import serial.tools.list_ports


#automatic port detection
ports = list(serial.tools.list_ports.comports())
for p in ports:
    #print(p)
    if "OpenMV" in p[1]:   
      #print(p[0])
      ser = serial.Serial()
      ser.baudrate = 11520
      ser.port = p[0]
      ser.open()
      while(1):
        value= ser.readline()
        pyautogui.click(pyautogui.position()) 
        #print(value)
        pyautogui.typewrite(str(value[0:17]))