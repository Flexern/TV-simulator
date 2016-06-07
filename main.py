#!/usr/bin/env python

import tvProgram

filename='tvDevices.txt'
try:
	with open(filename, 'r') as file: # read a list of lines into data
		data = file.readlines()
		
		livingRoomTV = tvProgram.TV( data[0].rstrip(), data[1].rstrip(), data[2].rstrip(), int(data[3].rstrip()) )
		kitchenTV = tvProgram.TV( data[0+5].rstrip(), data[1+5].rstrip(), data[2+5].rstrip(), int(data[3+5].rstrip()) )
		
except IOError:
	print('Something went wrong...')

def main():
	global tv, device
	while True:
		try:
			val=int(input('''
*** Welcome to TV-simulator! Here we use two TV devices ***

1. Living room TV
2. Kitchen TV
3. Power off
Your choice: '''))			
			
			if(val==1):
					device=0 
					tv=livingRoomTV
					tvMenu()

			elif(val==2):
					device=1
					tv=kitchenTV
					tvMenu()

			elif(val==3):
					break
					file.close()
					quit()
					
			else:
				# Error control numbers
				print('Choose a number between 1 and 3')
		
		except BaseException as err:
			# Error control letters
			print('Choose a number between 1 and 3')

def tvMenu():
	# Displays second menu
	while True:
		try:
			print(tv)
			menuChoice=int(input('''
1. Change channel
2. Lower volume 
3. Higher volume
4. Back to main menu
Your choice: '''))	
			if(menuChoice==1):
				changeChannel()
			elif(menuChoice==2):
				tv.lowerVolume()
				
				data[3+5*device]=str(tv.volume)+'\n'
				with open('tvDevices.txt', 'w') as file:
					file.writelines(data)
			elif(menuChoice==3):
				tv.higherVolume()
				data[3+5*device]=str(tv.volume)+'\n'
				with open('tvDevices.txt', 'w') as file:
					file.writelines(data)
					
			elif(menuChoice==4):
				break
			else:
				# Error control "numbers"
				print('Choose a number between 1 and 4')
		except BaseException as err:
			# Error control "letters"
			print('Choose a number between 1 and 4')

def changeChannel():
	# Change channel and program
	while True:
		try:
			channelChoice=int(input('''
1. MTv: Music is life
2. Tv 3: MacGyver
3. Svt 1: Money is not everything
4. Kanal 4: Who Wants to Be a Millionaire?
Your choice: '''))		
			if(channelChoice==1):
				channel='MTv'
				program='Music is life'
			elif(channelChoice==2):
				channel='Tv 3'
				program='MacGyver'
			elif(channelChoice==3):
				channel='Svt 1'
				program='Money is not everything'
			elif(channelChoice==4):
				channel='4'
				program='Who Wants to Be a Millionaire?'
			else:
				# Error control numbers
				print('Choose a number between 1 and 4')
			
			data[1+5*device]=str(program)+'\n'
			data[2+5*device]=str(channel)+'\n'
			with open('tvDevices.txt', 'w') as file:
				file.writelines(data)
			tv.changeChannel(channel, program)
			break
							
		except BaseException as err:
			# Error control letters
			print('Choose a number between 1 and 4')
	

if(__name__ == '__main__'):
	main()
