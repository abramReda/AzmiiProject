
        ##########################################################################################################################################
        # Discription                                                                                                                            #
        #               this software is part from Azmii project,this  class is to control Hand in three position  UP/down/center       	 #
        #               our Hardwear configration for hand is one DC motor with three limit switch to locate the Hand Position                   #
	#		the motor is parment magnet DC with a geerBox and it will controll via our simple motor class  				 #
	#		the three limit switch are configer whene it pressed give zero volte and when it release it give 5 volt			 #
        ##########################################################################################################################################
        # Paremters:                                                                                                                             #
	#		LMUP , LMCENTER , LMDOWN >> are the three  Phisical PIN in GPIO that the limit switch conected to it			 #
	#		motorPin1 , MotorPin2 >> are the phisical  PINs wich control the motor dirction Where: 					 #
        #              		 Pin1 >> the 1st phisical bin conect to the 1st base of transestor wich actve the 1st relay                      #
        #              		 pin2 >> the 2nd phisical bin conect to the 2nd base of transestor wich actve the 2nd relay           		 #
        ##########################################################################################################################################
        # auther                                                                                                                                 #
        #               Eng:Ibram Reda                                                                                                           #
        ##########################################################################################################################################




import RPi.GPIO as GPIO
import motor


UP=1
CENTER =2
DOWN = 3
FLOATING =4


class Hand:
	def __init__(self , LMUP , LMCENTER , LMDOWN , motorPin1 , motorPin2):
		self.motor = motor.motor(motorPin1 , motorPin2)
		self.LMUP=LMUP
		self.LMCENTER=LMCENTER
		self.LMDOWN=LMDOWN
		self.virtualPosition = FLOATING

		#DECLAIT LIMIT SWITICHES AS INPUT

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(LMUP , GPIO.IN , pull_up_down = GPIO.PUD_UP)
		GPIO.setup(LMDOWN , GPIO.IN , pull_up_down = GPIO.PUD_UP)
		GPIO.setup(LMCENTER , GPIO.IN , pull_up_down = GPIO.PUD_UP)

		#inintal position of hand well be center
		self.virtualPosition = self.getCurrentPosition()
		self.lastPosition    = self.getCurrentPosition()
		self.center()





	def setPosition(self,desirdPosition):
		if desirdPosition == UP:
			self.up()
		elif desirdPosition == DOWN:
			self.down()

		elif desirdPosition == CENTER:
                        self.center()

		else :
			pass # TO DO : trow error rowng position u have only three positions UP=1,CENTER=2,DOWN=3



	def up(self):

		if self.getCurrentPosition() == UP:
			return
		else : #run motor until up position it will make callpration and re adjust
				self.motor.forward()
				self.runUntill(self.LMUP)
		self.virtualPosition = UP  #update virtial position


	def down(self):
		if self.getCurrentPosition() == DOWN:
                        return
                else:
                        if self.getCurrentPosition() != DOWN:
                                self.motor.backward()
				self.runUntill(self.LMDOWN)
               	self.virtualPosition = DOWN  #update virtial position



	def center(self):
		if self.getCurrentPosition() == CENTER:
                        return
                elif self.virtualPosition == UP:
                        if self.getCurrentPosition() != CENTER:
                                self.motor.backward()
		elif self.virtualPosition == DOWN:
                        if self.getCurrentPosition() != CENTER:
                                self.motor.forward()
		else:   #for floating position
			if self.getCurrentPosition() != CENTER:
                                self.motor.forward()
		self.runUntill(self.LMCENTER)
		self.virtualPosition = CENTER   #update virtial position




	def getCurrentPosition(self):
		#this method will return where which Limit switch is pressed
		#note that limitSwitch is active low pin
	        if  not GPIO.input(self.LMUP):
                    return UP

		if not GPIO.input(self.LMCENTER):
                    return CENTER

                if  not GPIO.input(self.LMDOWN):
                    return DOWN
		return FLOATING






	def runUntill(self,limitSwitchPos):
		#private methode
		if limitSwitchPos == self.LMUP:
			GPIO.remove_event_detect(self.LMDOWN)
                        GPIO.remove_event_detect(self.LMCENTER)
                        GPIO.add_event_detect(self.LMUP,GPIO.FALLING,callback=self.stopAndClear,bouncetime=300)

		elif limitSwitchPos == self.LMDOWN:
			GPIO.remove_event_detect(self.LMUP)
                        GPIO.remove_event_detect(self.LMCENTER)
                        GPIO.add_event_detect(self.LMDOWN,GPIO.FALLING,callback=self.stopAndClear,bouncetime=300)

		elif limitSwitchPos == self.LMCENTER:
			GPIO.remove_event_detect(self.LMDOWN)
	                GPIO.remove_event_detect(self.LMUP)
        	        GPIO.add_event_detect(self.LMCENTER,GPIO.FALLING,callback=self.stopAndClear,bouncetime=300)

		else :
			pass # TO DO :must throw error rowng pin thers no limit switch at limitswitchpos

	def stopAndClear(self,channal):
		#private method
		self.motor.stop()
		GPIO.remove_event_detect(channal)
		#UPDATE THE LAST POSITION TO ARM
		if channal == self.LMUP:
			self.lastPosition = UP
		elif channal == self.LMDOWN:
                        self.lastPosition = DOWN
		elif channal == self.LMCENTER:
                        self.lastPosition = CENTER



	def calibration(self):
		# dueto our system has no selfLock system , we make calibration
		# to be sure that our arm in the right position .
		# arm position can change dueto two forces  gravity or human force
		# unfortunaly our systm has no many point to detect where it exactly
		# if human force change it :( so we dont't calibrat aginst this force :(
		# we can treat gravity force :) because we know that force make our arm
		# slitly below the disrd point so we run motor to ritch the exact limitSwitch position
		if self.getCurrentPosition()== FLOATING:
			self.motor.forward() # becuse gravity always act to down
			if self.virtualPosition==UP:
				self.runUntill(self.LMUP)
			elif self.virtualPosition==CENTER:
                                self.runUntill(self.LMCENTER)
			elif self.virtualPosition==DOWN:
                                self.runUntill(self.LMDOWN)
			else :
				pass # TO DO : must throw error virtualPosition do't initalized , it must tack value in [1,2,3] 
