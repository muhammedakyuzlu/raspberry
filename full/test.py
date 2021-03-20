from motor_module import Motors , Motor
import lane_detection_module
from sensor import Sensor
import camera
import sys
import time
import cv2



CAMERA_PORT = 0

def main():

    startTime = time.time()

    img = camera.GetImg().getImg(display=False,)
    curve = lane_detection_module.getLaneCurve(img,display=2)
    print('curve',curve)
    print('Time ',time.time()-startTime)
    motor.move(0.5,curve,0)
    motor.forward(0.5,0)


    # motor.stop(1)

    #motor.move(-1,-0.5,0.2)
    #motor.move(1,-0.5,0.2)
    # motor.stop(1)

    # motor.move(1,0.5,0.1)
    # motor.stop(3)











if __name__ == '__main__':
    #MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom right
    motor = Motors(22,17,27,5,6,12,26,13,19,16,20,21)
    #motor = Motor(5,6,12)
    #print('fuck coding **************************************')
    # Sensor
    sensor = Sensor(pinTrigger=23,pinEcho=4)
    s = sensor.distance()

    try:
        while s > 10:
            startTime = time.time()
            s = sensor.distance()
            main()
            print ("Distance: %.1f cm" % s)
            print('Sensor Time ',time.time()-startTime)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        #sensor.close()
        motor.stop()
        motor.clean()
        sys.exit(0)
    except Exception:
        print('something went wrong')
        #sensor.close()
        motor.stop()
        motor.clean()
        sys.exit(0)
           

  

