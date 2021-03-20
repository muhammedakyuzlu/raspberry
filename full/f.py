import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



pin = [22,17,27,5,6,12,26,13,19,16,20,21]


for i in pin :
    GPIO.setup(i,GPIO.OUT)
    pwm = GPIO.PWM(i,100)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(4,GPIO.IN)
GPIO.cleanup()    

print('cleaned up!')
