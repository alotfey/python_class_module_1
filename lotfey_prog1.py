##########################################
# CS 1110A - Programming in Python       #
# Module 1 - Program 1 - Body Mass Index #
# Author: Ahmed Lotfey                   #
# Date:   20/18/2023                     #
##########################################

# Print the program title
print("Calculate Body Math Index (BMI)\n")

# Ask user for  weight
ask_weight = input("What is your weight in pounds? ")

# Ask user for height in inches
ask_height = input("What is your height in inches? ")

# Convert weight from lb to kg
lb_to_kg = int(ask_weight) / 2.2

# Convert heightfrom inches to meter
inches_to_meter = int(ask_height) * 0.0254

# Calculate PMI BMI = Weight (kg) ÷ Height (m)2
calculate_bmi = lb_to_kg / (inches_to_meter**2)


# print output message show the BMI result
print(
    f"\nAt a weight of {ask_weight} and height of {ask_height} inches,"
    f" Your BMI is {calculate_bmi:.1f}"
)

# print Done! with break line
print("\nDone!")
