import time
import RPi.GPIO as GPIO


leds = [11, 15]

GPIO.setmode(GPIO.BOARD)

for led in leds:
        GPIO.setup(led, GPIO.OUT)

try:
        for i in range(0,20):
                is_on = i % 2 == 0

                for j in range(len(leds)):
                        GPIO.output(leds[j], is_on)
                        is_on = not is_on

                print("LED ON = " + str(is_on))
                time.sleep(0.5)
finally:
        GPIO.cleanup()

