
import RPi.GPIO as GPIO
import time

# Xác đinh chân trên thiết bi Raspberry Pi Module B+ 
triggerPin = 4
echoPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

GPIO.output(triggerPin, True)
time.sleep(0.0001)
GPIO.output(triggerPin, False)
while GPIO.input(echoPin) == False:
    start = time.time() # thoi diem bst dau phat ra somg am
while GPIO.input(echoPin) == True: 
    end = time.time()   # thoi diem soong am nhan duoc tro lai do vat can phan xa song 
    
sigtime = ( end - start ) / 2
distance = sigtime / 0.0000291

print('Distance: {} cm'.format(distance)) 

GPIO.cleanup()



