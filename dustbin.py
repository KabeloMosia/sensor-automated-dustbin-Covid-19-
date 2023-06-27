
import RPi.GPIO as GPIO
import time 
##from beebotte import *

##bclient = BBT("ssaVKYWDarGFgNETsCAC7j5j", "aluha6YL3kWio6qAa2t4UW8B696klE2q")
##status_resource = Resource(bclient,'Dust','status')
##count_resource = Resource (bclient, 'Dust','counter')

GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 12 
GPIO_ECHO = 18
serve_motor=16
GPIO.setup(serve_motor,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

how_many_times = 0
servo = GPIO.PWM(16,50)
try:
 while True:

  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  servo.start(0)
  time.sleep(1)
  StartTime = time.time()
  StopTime = time.time()

  while GPIO.input(GPIO_ECHO) == 0:
   StartTime = time.time()

  while GPIO.input(GPIO_ECHO) == 1:
   StopTime = time.time()

  TimeElapsed = StopTime - StartTime
  distance = (TimeElapsed * 34300) / 2


  if distance<= 10 :
   how_many_times+=1
  
   print ("\nDistance from the object is ==> %.0f CM" % distance)
   print ("Opening the smart dustbin")
   servo.ChangeDutyCycle(7.5)
   time.sleep(2)
   servo.ChangeDutyCycle(0)
   print ("Dust thrown",how_many_times,"time")
   
  else:
   print ("\nDistance from the object is ==> %.0f CM" % distance)
   print ("Lid of the dustbin is covered")
   time.sleep(0.5)
except Exception:
  print("\nError while writing data to cloud")
except KeyboardInterrupt:
  print("\nThe automatic dustbin program is terminated!\n")
  p.stop()
  GPIO.cleanup()
