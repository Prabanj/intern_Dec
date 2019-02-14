# Untitled - By: CTS-TIH 1 - Tue Dec 11 2018

import pyb
from pyb import Pin
import sensor, image, time, math ,lcd
from pyb import LED
blue_led   = LED(3)
switch = Pin('P4', Pin.IN, Pin.PULL_NONE)
led = Pin('P9', Pin.OUT_PP, Pin.PULL_NONE)


while(True):

  if(switch.value()):
      led.high()

      sensor.reset()
      sensor.set_pixformat(sensor.RGB565)
      sensor.set_framesize(sensor.VGA)

      #lcd.set_backlight(True)
      sensor.set_windowing((200, 260)) # 2x Zoom
      sensor.skip_frames(time = 2000)

      sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
      sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...

      #clock = time.clock()
      lcd.init()
      while(switch.value()):
           #clock.tick()
           img = sensor.snapshot()

           matrices = img.find_datamatrices()
           for matrix in matrices:
               img.draw_rectangle(matrix.rect(), color = (255, 0, 0))
               myImage= image.Image("indication.ppm", copy_to_fb = True)
               lcd.display(myImage)
               pyb.delay(400)
               print(matrix.payload())

           if not matrices:
               qcode=img.find_qrcodes();
               for code in qcode:
                       img.draw_rectangle(code.rect(), color = (255, 0, 0))
                       myImage= image.Image("indication.ppm", copy_to_fb = True)
                       lcd.display(myImage)
                       pyb.delay(400)
                       print(code.payload())

               if not qcode:
                 bcode=img.find_barcodes();
                 for code in bcode:
                       img.draw_rectangle(code.rect(), color = (255, 0, 0))
                       myImage= image.Image("indication.ppm", copy_to_fb = True)
                       lcd.display(myImage)
                       pyb.delay(400)
                       print(code.payload())

           lcd.display(img) # Take a picture and display the image.s




  else:
      led.low()
      lcd.set_backlight(False)
      #lcd.deinit()
      #sensor.sleep(True)
