def calculate_time(seconds):
    time = str(int(seconds)/60).split('.')
    minutes = time[0]
    # set size of seconds less than 60
    seconds = int(time[1]).__str__()[:2]
    seconds = int(seconds)*60/100
    print(f"Length: {minutes} minutes {seconds} seconds")
