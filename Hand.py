


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

		#inintal podition of hand well be center
		self.virtualPosition = self.getCurrentPosition()
		self.center()




	def setPosition(self,desirdPosition):
		if desirdPosition == UP:
			self.up()
		elif desirdPosition == DOWN:
			self.down()

		elif desirdPosition == CENTER:
                        self.center()





	def up(self):

		if self.virtualPosition == UP:
			return

		else : #run motor until up position
			if self.getCurrentPosition() != UP:
				self.motor.forward()
				GPIO.remove_event_detect(self.LMDOWN)
				GPIO.remove_event_detect(self.LMCENTER)
				GPIO.add_event_detect(self.LMUP,GPIO.FALLING,callback=self.stopAndClear,bouncetime=300)

		self.virtualPosition = UP  #update virtial position


	def down(self):
		if self.virtualPosition == DOWN:
                        return
                else:
                        if self.getCurrentPosition() != DOWN:
                                self.motor.backward()
				GPIO.remove_event_detect(self.LMUP)
                                GPIO.remove_event_detect(self.LMCENTER)
				GPIO.add_event_detect(self.LMDOWN,GPIO.FALLING,callback=self.stopAndClear,bouncetime=300)

               	self.virtualPosition = DOWN  #update virtial position



	def center(self):
		if self.virtualPosition  == CENTER:
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
		GPIO.remove_event_detect(self.LMDOWN)
                GPIO.remove_event_detect(self.LMUP)

		GPIO.add_event_detect(self.LMCENTER,GPIO.FALLING,callback=self.stopAndClear,bouncetime=300)
                self.virtualPosition = CENTER   #update virtial position




	def getCurrentPosition(self):
	        if  not GPIO.input(self.LMUP):
                    return UP

		if not GPIO.input(self.LMCENTER):
                    return CENTER

                if  not GPIO.input(self.LMDOWN):
                    return DOWN
		return FLOATING

	def stopAndClear(self,channal):
		self.motor.stop()
		GPIO.remove_event_detect(channal)
