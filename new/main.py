from motor_module import Motors 
#import lane_dete

# # top left 
# TLMotor = Motor(22,17,27)
# # top right
# TRMotor = Motor(14,15,18)
# # buttom left
# BLMotor = Motor(26,13,19)
# # buttom right
# BRMotor = Motor(16,20,21)
 
# MOTORS: ENA IN1 IN2 :top left  top right buttom left  buttom right
motor = Motors(22,17,27,14,15,18,26,13,19,16,20,21) 


def main():

    #motor.move(Forward=True,speed=1,turn=0,t=3)
    #motor.stop(1)
    #motor.buttomMotors(speed=100,turn=0,t=0.1)
    #motor.topMotors(speed=100,turn=-90,t=3)
    
    
    motor.move(speed=1,turn=0.25,t=1)
    motor.move(speed=1,turn=-0.25,t=1)
    motor.move(speed=1,turn=1,t=1)
    motor.move(speed=1,turn=-1,t=1)
    motor.stop(1)
    #motor.move(Forward=True,speed=1,turn=0,t=3)
    #motor.stop(1)
    #motor.move(Forward=False,speed=1,turn=0.5,t=3)
 
if __name__ == '__main__':
    while True:
        main()
        
#  GPIO.cleanup()        
