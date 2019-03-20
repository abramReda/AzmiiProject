
from motor import *

class movement:

	def __init__(self,M11,M12,M21,M22):
		self.rightMotor = motor(M11,M12,False)
		self.leftMotor  = motor(M21,M22,False)



	def forward(self):
		self.rightMotor.forward()
		self.leftMotor.forward()
	def backward(self):
		self.rightMotor.backward()
                self.leftMotor.backward()


	def right(self):
		self.rightMotor.stop()
                self.leftMotor.forward()

	def left(self):
		self.rightMotor.forward()
                self.leftMotor.stop()

	def stop(self):
		self.rightMotor.stop()
                self.leftMotor.stop()

	def fastRight(self):
                self.rightMotor.backward()
                self.leftMotor.forward()
        def fastLeft(self):
                self.rightMotor.forward()
                self.leftMotor.backward()

