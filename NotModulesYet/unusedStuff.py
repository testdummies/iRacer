
last_time_check = datetime.now()
current_time = datetime.now()
time_difference = (current_time - last_time_check).total_seconds()


def refresh_time():
    global current_time
    global time_difference
    global last_time_check
    current_time = datetime.now()
    time_difference = (current_time - last_time_check).total_seconds()
    last_time_check = current_time

def print_Shit():
    refresh_time()
    print time_difference
    print type(time_difference)
