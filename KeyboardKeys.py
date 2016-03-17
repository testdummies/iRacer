import pygame
import time, sys

pygame.init()
pygame.display.set_mode((1,1))

keys_pressed = []
keys_released = []

key_is_pressed = False

counter = 0
while counter < 3:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			keys_pressed.append(chr(event.key))
			key_is_pressed = True

	if key_is_pressed:
		counter = counter + 1
		key_is_pressed = False

print str(keys_pressed)


