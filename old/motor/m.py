import RPi.GPIO as GPIO          
from time import sleep

# top left
tl1=17
tl2=27
tl_en=22

# top right
tr1=15
tr2=18
tr_en=14

# bottom  left
bl1=13
bl2=19
bl_en=26

# bottom right
br1=20
br2=21
br_en=16



GPIO.setmode(GPIO.BCM)


GPIO.setup(tl1,GPIO.OUT)
GPIO.setup(tl2,GPIO.OUT)
GPIO.setup(tl_en,GPIO.OUT)

GPIO.setup(tr1,GPIO.OUT)
GPIO.setup(tr2,GPIO.OUT)
GPIO.setup(tr_en,GPIO.OUT)

GPIO.setup(bl1,GPIO.OUT)
GPIO.setup(bl2,GPIO.OUT)
GPIO.setup(bl_en,GPIO.OUT)

GPIO.setup(br1,GPIO.OUT)
GPIO.setup(br2,GPIO.OUT)
GPIO.setup(br_en,GPIO.OUT)


    
def forward_high() :

    GPIO.output(tl1,GPIO.HIGH) 
    GPIO.output(tl2,GPIO.LOW) 
    GPIO.output(tl_en,GPIO.HIGH)     
    
    GPIO.output(tr1,GPIO.HIGH) 
    GPIO.output(tr2,GPIO.LOW) 
    GPIO.output(tr_en,GPIO.HIGH) 
    
    GPIO.output(bl1,GPIO.HIGH)
    GPIO.output(bl2,GPIO.LOW) 
    GPIO.output(bl_en,GPIO.HIGH) 
    
    GPIO.output(br1,GPIO.HIGH) 
    GPIO.output(br2,GPIO.LOW) 
    GPIO.output(br_en,GPIO.HIGH) 
    
print("Motor going to Start")

forward_high(0)

sleep(5)

print("Stopping motor")

GPIO.output(br_en,GPIO.LOW) # to stop the motor

GPIO.cleanup()


###################################
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
class motor():
    def __init__(self,Ena,In1,In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(0)
    def moveF(self,x=100,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        sleep(t)
    def moveB(self,x=100,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        sleep(t)
    def stop(self,t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)
 
motor1 = motor(2,3,4)
 
while True:
    
    motor1.moveF(30,2)
    motor1.stop(1)
    motor1.moveB(t=2)
    motor1.stop(1)
     
    '''
    for x in range(20,100):
        motor1.moveF(x,0.05)
        print(x)
    for x in range(100,20,-1):
        motor1.moveF(x,0.05)
        print(x)
    motor1.stop(5)
    '''
