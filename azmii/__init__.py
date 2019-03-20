


import Hand
import Head
import movement
import RPi.GPIO as GPIO

GPIO.cleanup() # reset GPIO


LeftHand = Hand.Hand(3,5,7,8,10)
RightHan = Hand.Hand(11,13,15,12,16)
BigHead  = Head.Head(19,21,23,22,24)
movesystem = movement.movement(22,24,36,35)

