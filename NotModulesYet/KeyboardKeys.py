import pygame
import time, sys

pygame.init()
pygame.display.set_mode((1,1))


#button, axis and hat definitions

#axis 0 is Thumbstick left (left (-1),right (1))
#axis 1 is Thumbstick left (up (-1),down (1))

#axis 3 is Thumbstick right (left (-1),right (1))
#axis 4 is Thumbstick right (up (-1),down (1))

#axis 2 is LT (Down (1),Released (-1)) 
#axis 5 is RT (up (-1),down (1))

#button 0 is A
#button 1 is B
#button 2 is X
#button 3 is Y
#button 4 is LB
#button 5 is RB
#button 6 is Back
#button 7 is Start
#button 8 is Xbox button
#button 9 is Left Stick button down
#button 10 is Right Stick button down

#hats down [0, -1]
#hats up [0, 1]
#hats left [-1, 0]
#hats right [1, 0]

# Initialize the joysticks
Joy0 = pygame.joystick.Joystick(0)
Joy0.init()

while True:
	for event in pygame.event.get():
		# Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
		#if event.type == pygame.JOYBUTTONDOWN:
			# for i in range( buttons ):
			# 	button = Joy0.get_button( i )
				#if button:
					#print("Joystick button pressed {0}".format(button))


		# if 0.5 <= 'value' triggers when the axes values are greater / equal to 0.5, with 1 being full on
		# if -0.5 >= 'value' triggers when the axes values are less / equal to -0.5, with -1 being full on

		# triggered when any of the axes are moved [see table above]
		# event.value returned as a float between 1 and -1 with 0 being center
		if event.type == pygame.JOYAXISMOTION:
			# left thumbstick x axis
			if event.axis == 0:
				pos = event.value
				# combo of using thumbstick and button together
				# Joy0.get_button(0) tests the exact button values [table above], True when pressed
				if 0.5 <= pos and Joy0.get_button(0) == True:
					print 'left stick right'
					print 'button A'
				if -0.5 >= pos:
					print 'left stick left'

			# left thumbstick Y axis
			if event.axis == 1:
				pos = event.value
				if 0.5 <= pos:
					print 'left stick down'
				if -0.5 >= pos:
					print 'left stick up'
			# right thumbstick x axis
			if event.axis == 3:
				pos = event.value
				if 0.5 <= pos:
					print 'right stick right'
				if -0.5 >= pos:
					print 'right stick left'
			# right thumbstick Y axis
			if event.axis == 4:
				pos = event.value
				if 0.5 <= pos:
					print 'right stick down'
				if -0.5 >= pos:
					print 'right stick up'
			# LT y axis
			if event.axis == 2:
				pos = event.value
				if 0.5 <= pos:
					print 'LT down'
			# RT y axis
			if event.axis == 5:
				pos = event.value
				if 0.5 <= pos:
					print 'RT down'

		# triggered when any of the hats [d-pad] are moved [see table above]
		# values are returned as a tuple from event.value eg [0,1]
		elif event.type == pygame.JOYHATMOTION:
				hat = event.value
				# checks the first value in the tuple
				if hat[0] == 1:
					print '1'
					print("event value axis 0: {}".format(hat)) 

		# triggered when any of the keyboard keys are pressed. event.key returned as an ASCII value. 
		# chr(value) gets the actual key pressed eg A
		elif event.type == pygame.KEYDOWN:
				keyPressed = event.key
				print 'key pressed {0}'.format(chr(keyPressed))
				# check for a specific key (Esc)
				if event.key == pygame.K_ESCAPE:
					sys.exit()


