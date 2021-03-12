import RPi.GPIO as GPIO
import time
import sys

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)


class Sensor():

	def __init__(self,pinTrigger,pinEcho):
		self.pinTrigger=pinTrigger
		self.pinEcho=pinEcho
		# set GPIO input and output channels
		GPIO.setup(self.pinTrigger, GPIO.OUT)
		GPIO.setup(self.pinEcho, GPIO.IN)


	def distance(self):
		#print("\nTurning on ultrasonic distance detection...\n")
		# set Trigger to HIGH
		GPIO.output(self.pinTrigger, True)
		# set Trigger after 0.01ms to LOW
		time.sleep(0.00001)
		GPIO.output(self.pinTrigger, False)

		startTime = time.time()
		stopTime = time.time()

		# save start time
		while 0 == GPIO.input(self.pinEcho):
			startTime = time.time()

		# save time of arrival
		while 1 == GPIO.input(self.pinEcho):
			stopTime = time.time()

		# time difference between start and arrival
		TimeElapsed = stopTime - startTime
		# multiply with the sonic speed (34300 cm/s)
		# and divide by 2, because there and back
		distance = (TimeElapsed * 34300) / 2

		#print ("Distance: %.1f cm" % distance)
		#time.sleep(1)
		
		return distance


	def close(self):
		#print("\nTurning off ultrasonic distance detection...\n")
		GPIO.cleanup([self.pinTrigger,self.pinEcho]) 
		#sys.exit(0)





if __name__ == '__main__':	
	while True:
		dis = Sensor(23,24)
		dis.distance()
		dis.close()
		time.sleep(2)
        