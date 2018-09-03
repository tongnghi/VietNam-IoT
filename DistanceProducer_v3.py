#!/usr/bin/python
import RPi.GPIO as GPIO
import threading, time, logging
import multiprocessing
from kafka import KafkaProducer, KafkaConsumer
# defind pin on Raspberry


triggerPin = 4
echoPin = 18
def dokhoangcach(triggerPin, echoPin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(triggerPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

    GPIO.output(triggerPin, True)
    time.sleep(0.0001)
    GPIO.output(triggerPin, False)
#    while GPIO.input(echoPin) == False:
    start = time.time() # thoi diem bst dau phat ra somg am
#    while GPIO.input(echoPin) == True: 

    time.sleep(2)

    end = time.time()   # thoi diem soong am nhan duoc tro lai do vat can phan xa song 
    
    sigtime = ( end - start ) / 2
    distance = sigtime / 0.0000291
    print('Distance: {} cm'.format(distance)) 
    GPIO.cleanup()
    return distance


class Producer(multiprocessing.Process):
        triggerPin = 4
        echoPin = 18
        msg = "THONG TIN TU HE THONG CANH BAO BANG SONG SIEU AM"

        def __init__(self):
            multiprocessing.Process.__init__(self)
            self.stop_event = multiprocessing.Event()
       
        def stop(self):
            self.stop_event.set()
                       
        def run(self):
            MSG = self.msg
            producer = KafkaProducer(bootstrap_servers='192.168.1.102:9094')
            while not self.stop_event.is_set():
                #distance = distance_mesuare(triggerPin, echoPin)
                producer.send('MYREP', MSG)
                #producer.send('MYREP', distance )
                #producer.send('MYREP', b"\xc2Hola, MumDOOOOOOOOOOO")
                time.sleep(1000)
            producer.close()
#=============================================


class Consumer(multiprocessing.Process):
        def __init__(self):
            multiprocessing.Process.__init__(self)
            self.stop_event = multiprocessing.Event()
       
        def stop(self):
            self.stop_event.set()
                       
        def run(self):
            consumer = KafkaConsumer(bootstrap_servers='192.168.1.102:9095', auto_offset_reset='earliest', consumer_timeout_ms=1000)
            consumer.subscribe(['MYREP'])
            while not self.stop_event.is_set():
                for mMessage in consumer:
                    #print(mMessage)
                    sendMail(mMessage)

                    if self.stop_event.is_set():
                        break
            consumer.close()


def sendMail(para):
    print("Mailling:")
    print(para)



def main():
    tasks = [
        Producer()
            ]

    for t in tasks:
        distance = dokhoangcach(4,18)
        t.msg = "Sound sensor............."
        t.msg = str(distance) 
        t.start()
    time.sleep(10000)
    print "Sleep 1s..."

    for task in tasks:
        t.stop()


    for task in tasks:
        t.join()


#    if __name__ == "__main__":
 #       logging.basicConfiga(format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s', level=logging.INFO)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s', level=logging.INFO)
    main()

#if (1==1):
print "Successfully sent email"
