#!/usr/bin/env python

class TV():
	def __init__(self, namn, channel='MTv', program='Music is life', volume=3):
		self.namn = namn
		self.channel = channel
		self.program = program
		self.volume = volume
	
	def __str__(self):
		return ('\n%s \nTV-program: %s \nChannel: %s \nSound volume: %s' % (self.namn, self.channel, self.program , self.volume) )

	def higherVolume(self):
		if(self.volume>=10):
			self.volume=10
		else:
			self.volume += 1
	
	def lowerVolume(self):
		if(self.volume<=0):
			self.volume=0
		else:
			self.volume -= 1
			
	def changeChannel(self, channel, program):
		self.channel = channel
		self.program = program




