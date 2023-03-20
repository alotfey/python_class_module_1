#######################################
# CS 1110A - Programming in Python    #
# Module 1 - Exercise 1 - Alarm Clock #
# Author: Ahmed Lotfey                #
# Date:   03/17/2023                  #
#######################################

# convert time format from 24 hours to 12 hours
def convert_time_12hr(time):
    if time > 12 and time < 24:
        time = time % 12
        time_12hr = f"{time} pm"
    elif time < 12 and time > 0:
        time_12hr = f"{time} am"
    elif time == 24:
        time_12hr = "12 am"
    else:
        raise IndexError("You can only covert time 1 to 24")
    return time_12hr


# convert time format from 12 hours to 24 hours
def convert_time_24hr(time):
    am_pm = time.split(" ")[1]
    time_now = int(time.split(" ")[0])
    if am_pm == "am" and time != "12 am" and time_now < 12:
        time_now_24hr = time_now
    elif am_pm == "pm" and time != "12 pm" and time_now < 12:
        time_now_24hr = time_now + 12
    elif time == "12 am":
        time_now_24hr = time_now + 12
    elif time == "12 pm":
        time_now_24hr = time_now
    else:
        raise IndexError("Wrong time should be 12hr input example: 12 am, 1pm")
    return time_now_24hr


# start time (current time)
start_time_12hr = "5 pm"

# start time in 24 hours format
start_time_24hr = convert_time_24hr(start_time_12hr)

# alarm ring end time by hours (duration time to alarm ring)
alarm_duration_time = 172

# Calculate remain time in days
remain_days = round(alarm_duration_time / 24)

# Alarm time ring at 24 hours system
alarm_ring_time = (start_time_24hr + alarm_duration_time) % 24

# Alarm time ring at 12 hours system
alarm_ring_time_12hr = convert_time_12hr(alarm_ring_time)

# Title of the program and new line break
print("Alarm Clock, Part 1 \n")

# Print time now message
print(f"Right now, it is {start_time_12hr}")

# Print time remaining message
print(
    f"The alarm clock will ring after {alarm_duration_time} hours which is"
    f" {remain_days} days from now at {alarm_ring_time_12hr}"
)

# print done message with new line
print("\nDone!")
