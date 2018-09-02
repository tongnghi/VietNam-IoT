
import RPi.GPIO as GPIO
import time

triggerPin = 4
echoPin = 18

ledPin = 4
movePin = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, GPIO.HIGH)

while True:
    i=GPIO.input(21)
    if  i==0: 
        print('NOT INTRUDERS',i)
        #time.sleep(1)
    else: 
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
        #time.sleep(1)

#time.delay(2)
#GPIO.cleanup()


#        GPIO.output(ledPin, GPIO.LOW)

