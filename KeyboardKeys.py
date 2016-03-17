import pygame
import time, sys

pygame.init()
pygame.display.set_mode((1,1))

keys_pressed = []
button_pressed = []
keys_multiple = []

key_is_pressed = False
multiple = False
button_is_pressed = False

# Initialize the joysticks
Joy0 = pygame.joystick.Joystick(0)
#pygame.joystick.init()
Joy0.init()

counter = 0
buttonCounter = 0
while counter < 3 and buttonCounter < 3:
	
	buttons = Joy0.get_numbuttons()
	for event in pygame.event.get():
		# Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
		if event.type == pygame.JOYBUTTONDOWN:
			for i in range( buttons ):
				button = Joy0.get_button( i )
				if button:
					button_pressed.append(event.button)
					button_is_pressed = True

			print("Joystick button pressed.")

		elif event.type == pygame.KEYDOWN:
				keys_pressed.append(chr(event.key))
				key_is_pressed = True

	if key_is_pressed:
		counter = counter + 1
		key_is_pressed = False

	if button_is_pressed:
		buttonCounter = buttonCounter + 1
		button_is_pressed = False


print str(keys_pressed)
print str(button_pressed)

if 0 in button_pressed:
	print 'A was pressed'


