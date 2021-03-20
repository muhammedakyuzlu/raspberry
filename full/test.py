from motor_module import Motors 
#import lane_detection_module
#from sensor import Sensor
#import lane_detection_module
#import camera
import sys

#CAMERA_PORT = 0

def main():
    # motor.move(0.5,0,1)
    # motor.stop(1)
    
    #motor.move(-1,-0.5,0.2)
    #motor.move(1,-0.5,0.2)
    # motor.stop(1)

    # motor.move(1,0.5,0.1)
    #motor.stop(3)

if __name__ == '__main__':

    #MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom right
    motor = Motors(22,17,27,5,6,12,26,13,19,16,20,21)
    
    # Sensor
    #sensor = Sensor(pinTrigger=23,pinEcho=4)


    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        #sensor.close()
        motor.stop()
        sys.exit(0)
    except Exception:
        print('something went wrong')
        #sensor.close()
        #motor.stop()
        sys.exit(0)
           

  

