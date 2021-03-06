from motor_module import Motors 
import lane_detection_module
from sensor import Sensor
import lane_detection_module
import camera
import sys
import multiprocessing,time
import time
import glob
import RPi.GPIO as GPIO
from time import sleep
import new_lane_line
import cv2
import asyncio


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin = [22,17,27,5,6,12,26,13,19,16,20,21]

# the camera port 0 or 1
CAMERA_PORT = 0
# # MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom righ
#motor = Motors(22,17,27,5,6,12,26,13,19,16,20,21)
# Sensor
sensor = Sensor(pinTrigger=23,pinEcho=4)


def go():
    # MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom right
    motor = Motors(22,17,27,5,6,12,26,13,19,16,20,21)
    a=0
    while True:
        # get image
        img = camera.GetImg().getImg()
        # if image got lost 
        if img is None :
            raise Exception("image got lost")
        # get curve from image by detecting the lane lines
        # curve = lane_detection_module.getLaneCurve(img,display=0)
        # print("curve: ",curve)
        # if curve>0 :
        #     turn =1
        # elif curve<0:
        #     turn=-1  
        # else:
        #     turn =0      
        # motor.move(speed=1,turn=0,t=3)
        #time.sleep(3)
        # img = new_lane_line.vid_pipeline(img)   
        # cv2.imshow('a',img)

        # motor.stop(t=10)
        motor.move(speed=1,turn=0,t=2)
        motor.move(speed=0.8,turn=0.2,t=0.2)
        motor.move(speed=1,turn=0,t=1)
        motor.stop(t=5)


        if cv2.waitKey(1) & 0xFF == 27:
            print('\n\nThe End')
            cv2.destroyAllWindows()
     
            break 


def force_to_stop(q):
    distance = sensor.distance()
    print ("Distance: %.1f cm" % distance)

    q.put(distance)


if __name__ == '__main__':
    try:
        q = multiprocessing.Queue()
        p1 = multiprocessing.Process(target = go)
        p1.start()
        while True:
            p2 = multiprocessing.Process(target = force_to_stop,args=[q])
            p2.start()
            p2.join()
            if q.get()  < 10 :
                p1.terminate()
                print('force to stop')
                sensor.close()
                #motor.stop()

                for i in pin :
                    GPIO.setup(i,GPIO.OUT)
                    pwm = GPIO.PWM(i,100)
                GPIO.setup(23,GPIO.OUT)
                GPIO.setup(4,GPIO.IN)
                GPIO.cleanup()    

                print('cleaned up!')    

                sys.exit(0)
                break
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        sensor.close()
        #motor.stop()
        sys.exit(0)
    except Exception:
        print('something went wrong')
        sensor.close()
        #motor.stop()
        sys.exit(0)
           

  

