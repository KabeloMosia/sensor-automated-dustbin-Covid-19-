import RPi.GPIO as GPIO 
import time 

servo_data_pin = 16 
standard_frequency = 50
left =1.5
right = 7
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(servo_data_pin, GPIO.OUT) 
p = GPIO.PWM(servo_data_pin,standard_frequency) 

print ("\n* At the bginning, moving to 180 degrees *")
p.start(1) 
time.sleep(1)

try:
 while True:
  print ("\nTurning to -90 degrees")
  p.ChangeDutyCycle(left) 
  time.sleep(2)

  ##print ("\nTurning to 180 degrees")
  ##p.ChangeDutyCycle(right) 
  ##time.sleep(2)
except KeyboardInterrupt: 
 print("\n Sorry! The program is interrupted.\n")
 p.stop() 
 GPIO.cleanup()
 