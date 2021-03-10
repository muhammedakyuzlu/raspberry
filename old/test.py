from gpiozero import LED

import time

led = LED(18)

for i in range(100) :
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
