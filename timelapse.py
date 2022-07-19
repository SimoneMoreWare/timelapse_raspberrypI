from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera ()
camera.resolution = (1920, 1080)

for i in range(20):
 camera.capture(‘/home/pi/Desktop/timelapse/image{0:04d}.jpg’.format(i))
 sleep(2)

system(‘convert -delay 1 -loop 0 home/pi/Desktop/timelapse/image*.jpg animation.gif’)
