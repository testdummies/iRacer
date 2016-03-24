import time
from datetime import datetime
import pygame
import time, sys

pygame.init()
pygame.display.set_mode((1,1))

keyboard_Controls = dict()# this provides lookup for values of actions
keyboard_Controls["Steer Left"] = "A"
keyboard_Controls["Steer Right "] = "D"
keyboard_Controls["Accelerate"] = "W"
keyboard_Controls["Break/Reverse"] = "S"
keyboard_Controls["Hand Break "] = "space" #SPACE
keyboard_Controls["N.O.S "] = "left shift"
keyboard_Controls["Transmission"] = "caps lock"
keyboard_Controls["Gear Down"] = "down"
keyboard_Controls["Gear Up"] = "up"
keyboard_Controls["Cruise Control"] = "left ctrl"
keyboard_Controls["Record Movements On"] = "-"
keyboard_Controls["Record Movements Off"] = "="

def readCurrentControls(dictionary):    # this reads dictionary that is sent
    for action,bound_key in dictionary.items():
        print "Action: %-*s  Key: %s" % (20,action,bound_key)

#check if bound key is in dictionary
#http://stackoverflow.com/questions/8214932/how-to-check-if-a-value-exists-in-a-dictionary-python
def check_if_exists(dictionary,key_value):    #checks if key is in the dictionary True/False
    return key_value in dictionary.values() #can check keys also
    #return dictionary.has_value(key)

def action_lookup(dictionary,action_key):
    return dictionary.get(action_key)
    #https://docs.python.org/2/library/stdtypes.html#dict.get
    #get(key[, default])
#Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

    #try:
    #    return dictionary[key]  #returns name for key in dictionary
    #except:
    #    return "invalid key" #returns invalid
#def rebind_action(dictionary,action,new_key):
def bind_key(dictionary,action,action_key):
    dictionary[action] = action_key

def gen_lookup_dictionary(dictionary):
    return dict((v,k) for k, v in dictionary.iteritems()) # this provides lookup for names of actions

inverted_keyboard_Controls = gen_lookup_dictionary(keyboard_Controls)
readCurrentControls(keyboard_Controls)
'''readCurrentControls(inverted_keyboard_Controls)'''
'''
print check_if_exists(keyboard_Controls,"S")
print action_lookup(inverted_keyboard_Controls,"S")
print check_if_exists(keyboard_Controls,"space")
print action_lookup(inverted_keyboard_Controls,"space")
print check_if_exists(keyboard_Controls," ")
print action_lookup(inverted_keyboard_Controls," ")
'''
active_action = action_lookup(inverted_keyboard_Controls,"S")   #looks up which action to change
new_key_input = "Z" #sets new key (this would be from read character stuff.)
bind_key(keyboard_Controls,active_action,new_key_input) #prints new keyboard mapping. On every key change
#inverse needs to be generated
inverted_keyboard_Controls = gen_lookup_dictionary(keyboard_Controls)

print "=================="
readCurrentControls(keyboard_Controls) #reads updated key







'''
def readKey(control_list):
    tmp_list = control_list
    print "Input key for :"+
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == enter:
                print "exiting"
            else:
                tmp_list.append(event.key)


keysInUse = []
def rebindKey(actionName):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == enter:
                print "exiting"
            else:
                actionName = event.key

def unbindKey(actionName):
    actionName

def print
'''
