import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
class Motor():

    def __init__(self,Ena,In1,In2):
        # speed
        self.Ena = Ena
        # direction
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        # 100 is frequency
        self.pwm = GPIO.PWM(self.Ena, 100)
        # init speed is zero
        self.pwm.start(0)


    def moveF(self,x=100):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)



    def moveB(self,x=100):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
  


    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.cleanup()

 



class Motors():

    def __init__(self,\
                    TLEna,TLIn1,TLIn2,\
                    TREna,TRIn1,TRIn2,\
                    BLEna,BLIn1,BLIn2,\
                    BREna,BRIn1,BRIn2):
                    
        # ENA speed  IN1,2 direction pwm frequency
        
        self.TLMotor = Motor(TLEna,TLIn1,TLIn2)
        self.TRMotor = Motor(TREna,TRIn1,TRIn2)
        self.BLMotor = Motor(BLEna,BLIn1,BLIn2)
        self.BRMotor = Motor(BREna,BRIn1,BRIn2)
        
        
    def move(self,speed=0.5,turn=0,t=0):
        speed *=100
        # turn *=90
        # left =  speed - turn
        # right = speed + turn 

        # if left>100: left=100
        # elif left<-100: left= -100
        # if right>100: right=100
        # elif right<-100: right= -100
        
        if speed > 0 :
            #forward right
            if turn > 0 :
                self.TLMotor.moveF(speed)
                self.BRMotor.moveB(speed)
                self.BLMotor.moveF(speed)
                self.TRMotor.moveB(speed)
                
                #self.TRMotor.moveB(abs(speed))
                #self.BLMotor.moveB(abs(speed))
            #forward left
            elif turn <0 :
                self.TLMotor.moveB(speed)
                self.TRMotor.moveF(speed)
                self.BRMotor.moveF(speed)
                self.BLMotor.moveB(speed)
               
            #forware streat 
            else :
                self.TLMotor.moveF(speed)
                self.TRMotor.moveF(speed)
                self.BLMotor.moveF(speed)
                self.BRMotor.moveF(speed)


        else :
            #backward right
            if turn > 0 :
                self.TLMotor.moveB(abs(speed))
                self.BRMotor.moveB(abs(speed))
            
            #backward left
            elif turn <0 :
                self.TRMotor.moveB(abs(speed))
                self.BLMotor.moveB(abs(speed))
            
            #backward streat 
            else :
                self.TLMotor.moveB(abs(speed))
                self.TRMotor.moveB(abs(speed))
                self.BLMotor.moveB(abs(speed))
                self.BRMotor.moveB(abs(speed))
        sleep(t)
    def stop(self,t=0):
        self.TLMotor.stop()
        self.TRMotor.stop()
        self.BLMotor.stop()
        self.BRMotor.stop()
        sleep(t)
