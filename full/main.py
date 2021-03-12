#from motor_module import Motors 
import lane_detection_module
#from sensor import Sensor
import lane_detection_module
import camera


CAMERA_PORT = 1

def main():
    distance = sensor.distance()
    print ("Distance: %.1f cm" % distance)



if __name__ == '__main__':

    

    # MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom right
    #motor = Motors(22,17,27,14,15,18,26,13,19,16,20,21) 

    # Sensor
    #sensor = Sensor(pinTrigger=23,pinEcho=24)




    while True:

        # get image
        img = camera.getImg()

        # if image got lost break
        if img is None :
             break

        # get curve from image by detecting the lane lines
        curve = lane_detection_module.getLaneCurve(img,display=0)
        
        print(curve)

    # for i in range(500):
    #     main()
    #sensor.close()

