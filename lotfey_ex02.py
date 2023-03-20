#######################################
# CS 1110A - Programming in Python    #
# Module 1 - Exercise 2 - Alarm Clock #
# Author: Ahmed Lotfey                #
# Date:   03/18/2023                  #
#######################################

# Title of the program and new line break
print("Alarm Clock, Part 2 \n")

# Ask the user for the time now (in 24 hour)
ask_time_now = input("What time is it now (in 24-hour notation): ")

# Ask the user how many hours the alarm go off
ask_alarm_off = int(input("How many hours from now should the alarm go off? "))

# The  alarm ring time
alarm_ring = (int(ask_time_now[0:2]) + ask_alarm_off) % 24

# Convert user input time to clock time format
def user_time_formating(time):
    if int(ask_time_now[0:2]) < 9 and int(ask_time_now[0:2]) >= 0:
        time_now = f"0{time}00"
    elif int(ask_time_now[0:2]) > 9 and int(ask_time_now[0:2]) < 25:
        time_now = f"{time}00"
    else:
        raise IndexError("wrong time format")
    return time_now


# Time in clock format (0300)
time_now_update = user_time_formating(alarm_ring)

# Calculate remain time in days
days_numbers = round(ask_alarm_off / 24)

# Print when the akarn will ring
print(
    f"The alarm clock will ring {days_numbers} days from"
    f" now at {time_now_update} hours"
)

# Print done message with new line
print("\nDone!")
