import pygame
import time, sys

pygame.init()
pygame.display.set_mode((1,1))

#
'''
while True:
	for event in pygame.event.get():

		# triggered when any of the keyboard keys are pressed. event.key returned as an ASCII value.
		# chr(value) gets the actual key pressed eg A
		if event.type == pygame.KEYDOWN:
			keyPressed = event.key
			try:
				print 'key pressed {0}'.format(chr(keyPressed))
			except:
				print "out of range of char"
			# check for a specific key (Esc)
			if event.key == pygame.K_ESCAPE:
				sys.exit()
'''
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			keyPressed = event.key
			if keyPressed == pygame.K_ESCAPE:
				sys.exit()
			if keyPressed == pygame.K_w:
				accelerate_forward = True
			if keyPressed == pygame.K_s:
				accelerate_reverse = True
			set_acceleration() # number
			print 'key pressed {0}'.format(chr(keyPressed))
