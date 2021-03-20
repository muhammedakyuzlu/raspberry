from motor_module import Motors 
import lane_detection_module
from sensor import Sensor
import lane_detection_module
import camera
import sys


# the camera port 0 or 1
CAMERA_PORT = 0
# MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom right
motor = Motors(22,17,27,5,6,12,26,13,19,16,20,21)
# Sensor
sensor = Sensor(pinTrigger=23,pinEcho=4)


def main():

    # get image
    img = camera.getImg()

    # if image got lost 
    if img is None :
        raise Exception("image got lost")

    # get curve from image by detecting the lane lines
    curve = lane_detection_module.getLaneCurve(img,display=0)
    
    print(curve)

    distance = sensor.distance()
    
    print ("Distance: %.1f cm" % distance)

    motor.move()
    


if __name__ == '__main__':
    try:
        while True:
            main()
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
           

  

