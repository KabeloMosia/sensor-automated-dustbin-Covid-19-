import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
 
GPIO_TRIGGER = 12 
GPIO_ECHO = 18
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
print ("\nPlease wait the distance measurement will start now.\n")
time.sleep(2)
print ("* Measurement Started *\n")
try:
 while True:
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  StartTime = time.time()
  StopTime = time.time()

  while GPIO.input(GPIO_ECHO) == 0:
   StartTime = time.time()

  while GPIO.input(GPIO_ECHO) == 1:
   StopTime = time.time()

  TimeElapsed = StopTime - StartTime
  distance = (TimeElapsed * 34300) / 2
  print ("The distance from the object is = %.1f cm" % distance)
  time.sleep(1.5)
 
except KeyboardInterrupt:
  print("\nMeasurement stopped by the User.\n")
  GPIO.cleanup()

