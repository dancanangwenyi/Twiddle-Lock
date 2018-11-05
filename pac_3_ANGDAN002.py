#	Written by Dancan Angwenyi
# 	ANGDAN002
#	prac 3 GPIOs

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

push1 = 17
push2 = 27
push3 = 22
led = 4

GPIO.setup(push1,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(push2,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(push3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

BS = False #keeps track of button state
bright = 0 #variable that changes duty cycle
pwm = GPIO.PWM(led,50)
some = pwm.start(0)

while(1):

	if GPIO.input(push1)==0:
		print ("Button 1 was pressed")
		if (BS == False and bright<100):
			BS = True
			print (BS)
			pwm.start(100)
			sleep(.5)
		else:
			BS=False
			print (BS)
			pwm.start(0)
			sleep(.25)

		#GPIO.output(led,BS)

	if GPIO.input(push2)==0:

		print ("Button 2 was pressed")
		sleep(.25)
		print (bright)


		if bright ==0:
			pwm.start(100)
			bright=98

		else:
			bright = bright -14
		pwm.ChangeDutyCycle(bright)

	if GPIO.input(push3)==0:

		print( "Button 3 was pressed")
		print (bright)

		sleep(.25)
		if bright==90:
			pwm.start(0)
			bright =0

		# if( bright < 89.25):
		#	pwm.start(0)
		#	bright=0
		else:
			bright= bright+10
		pwm.ChangeDutyCycle(bright)

