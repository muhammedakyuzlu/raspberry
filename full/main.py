from motor_module import Motors 
import lane_detection_module
from sensor import Sensor
import lane_detection_module
import camera
import sys
import multiprocessing,time

# the camera port 0 or 1
CAMERA_PORT = 0
# MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom right
motor = Motors(22,17,27,5,6,12,26,13,19,16,20,21)
# Sensor
sensor = Sensor(pinTrigger=23,pinEcho=4)


def go():
    while True:
        # get image
        img = camera.GetImg().getImg()
        # if image got lost 
        if img is None :
            raise Exception("image got lost")
        # get curve from image by detecting the lane lines
        curve = lane_detection_module.getLaneCurve(img,display=2)
        print("curve: ",curve)
        motor.move()

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
                motor.stop()
                sys.exit(0)
                break
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        sensor.close()
        motor.stop()
        sys.exit(0)
    except Exception:
        print('something went wrong')
        sensor.close()
        motor.stop()
        sys.exit(0)
           

  

