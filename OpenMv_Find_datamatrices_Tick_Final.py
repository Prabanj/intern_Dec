# Find Data Matrices w/ Lens Zoom Example
#
# This example shows off how easy it is to detect data matrices using the
# OpenMV Cam M7. Data matrices detection does not work on the M4 Camera.

import sensor, image, time, math
from pyb import UART
from pyb import LED


import pyb

red_led   = LED(2)



sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA)
sensor.set_windowing((320, 240)) # 2x Zoom
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
clock = time.clock()

thresholds = (220, 255)


while(True):
    clock.tick()
    img = sensor.snapshot()
    #img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
    #img.mean(1, threshold=True, offset=15, invert=True)

    #img = sensor.snapshot().binary([thresholds], invert=False, zero=True)


    matrices = img.find_datamatrices()
    for matrix in matrices:
        img.draw_rectangle(matrix.rect(), color = (255, 0, 0))
        #image.load_decriptor("E:\Intern'18_Sanj\Python Prog\Untitled.jpg")
        myImage = image.Image("download.ppm", copy_to_fb = True)
        #print(myImage)
        print_args = (matrix.payload())
        print(print_args)
        red_led.on()
        pyb.delay(500)
        red_led.off()
        pyb.delay(500)
        #uart = UART(3, 9600)
        #uart.write('1')
        #print(matrix.payload())
        #red_led.on()
        #pyb.delay(500)
        #red_led.off()
        #pyb.delay(2000)
