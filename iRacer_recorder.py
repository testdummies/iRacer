car_recorder = False # on/off for recording movments.
car_player = False


action_sequence = []    #maybe useful lists..not sure yet
duration_sequence = []
timestamp_sequence = []

def recorder(command, duration, timestamp):
    #add commands + duration of sleep that corresponds
    #to the command issued to lists
    #record timestamp of the command.
    #get difference between timestamps and maybe use it as 'wait/sleep' before

def player():
    #get difference between timestamps and maybe use it as 'wait/sleep' before
    #execute commands in order with timings?

def recording_status(): #changes values for recording
    if car_recorder:
        car_player = False
    if car_player:
        car_recorder = False
