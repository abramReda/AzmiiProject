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


	


