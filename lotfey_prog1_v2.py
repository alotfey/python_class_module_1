#############################################
# CS 1110A - Programming in Python          #
# Module 1 - Program 1 V2 - Body Mass Index #
# Author: Ahmed Lotfey                      #
# Date:   20/18/2023                        #
#############################################

# Print the program title
print("Calculate Body Math Index (BMI)\n")

# Ask user for  weight
while True:
    ask_weight = input("What is your weight in pounds? ")
    if ask_weight.isnumeric():
        break
    else:
        print(f"You can not enter non numeric {ask_weight} please input numeric only")

# Ask user for height in inches
while True:
    try:
        ask_height = input("What is your height in feet/inches , Example: 5/6? ")
        height_feet = ask_height.split("/")[0]
        height_inch = ask_height.split("/")[1]
        if height_feet.isnumeric() and height_inch.isnumeric():
            break
        else:
            print(
                "Please make sure you sure you enter the correct formate feet/inches Example: 5/6"
            )
    except:
        print(
            "Please make sure you sure you enter the correct formate feet/inches Example: 5/6"
        )
# Convert weight from lb to kg
lb_to_kg = int(ask_weight) / 2.2

# conver feet and inches to meter
feet_inch_to_meter = (int(height_feet) * 0.3048) + (int(height_inch) * 0.0254)


# Calculate PMI BMI = Weight (kg) ÷ Height (m)2
calculate_bmi = lb_to_kg / (feet_inch_to_meter**2)

# evaluate the bmi category
def bmi_categories():
    if calculate_bmi < 18.5:
        return "Underweight"
    elif calculate_bmi > 18.5 and calculate_bmi < 24.9:
        return "Normal Weight"
    elif calculate_bmi > 25.0 and calculate_bmi < 29.9:
        return "Overweight"
    elif calculate_bmi >= 30.0:
        return "Obese"
    else:
        raise IndexError("unknow category")


# print output message show the BMI result
print(
    f"\nAt a weight of {ask_weight} and height of {height_feet} feet and {height_inch} inches,"
    f" Your BMI is {calculate_bmi:.1f} and your BMI category is {bmi_categories()}"
)

# print Done! with break line
print("\nDone!")
