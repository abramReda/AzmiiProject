
	##########################################################################################################################################
        # Discription                                                                                                                            #
        #               this software is part from Azmii project,this  class is for simple motor control via two  RELAYs  foroward/backward/OFF  #
        #                we don't use speed control or PWM                                                                                       #
        ##########################################################################################################################################
        # Paremters:                                                                                                                             #
        #               Pin1 >> the 1st phisical bin conect to the 1st base of transestor wich actve the 1st relay                               #
        #               pin2 >> the 2nd phisical bin conect to the 2nd base of transestor wich actve the 2nd relay                               #
        #               trigeractive >> i assumwed that the two transistors are NPN type then they  will  activated by haigh volt in its  bases  #
        #               make it false if you use the two transistor of PNP type to invert the Logic                                              #
        ##########################################################################################################################################
	# auther 																 #
	#		Eng:Ibram Reda														 #
	##########################################################################################################################################

import RPi.GPIO as GPIO

class motor:
	def __init__(self , pin1 , pin2 , trigeractive = True):
		self.PIN1 = pin1
		self.PIN2 = pin2
		self.trigerActive = trigeractive
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.PIN1 , GPIO.OUT)
		GPIO.setup(self.PIN2 , GPIO.OUT)
		GPIO.output(self.PIN1  ,  not self.trigerActive)
		GPIO.output(self.PIN2  ,  not self.trigerActive)

	def forward(self):
		GPIO.output(self.PIN1  ,      self.trigerActive)
                GPIO.output(self.PIN2  ,  not self.trigerActive)

	def backward(self):
                GPIO.output(self.PIN1  , not  self.trigerActive)
                GPIO.output(self.PIN2  ,   self.trigerActive)

	def stop(self):
                GPIO.output(self.PIN1  ,  not self.trigerActive)
                GPIO.output(self.PIN2  ,  not self.trigerActive)




