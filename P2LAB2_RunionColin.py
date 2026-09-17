# Colin Runion
# 9/17/2026
# Use a dictionary to determine amount of fuel needed from user inputs

# Create the dictionary - cars are the keys and mpgs are the values
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Select only the keys
keys = cars.keys()

# Display keys to user
print()
print(keys)

# Get a car choice from the user
car_choice = input("Enter a car to see it's mpg: ")

# Using car_choice, pull the associated mpg from dictionary
mpg = cars[car_choice]

# Display car choice and mpg back to user
print(f"The {car_choice} gets {mpg} mpg.")

# Get miles to drive from user as a float
miles = float(input(f"How many miles will you drive the {car_choice}? "))

# Calculate gallons of gass needed
gallons = miles/mpg

# Display
print(f"{gallons:2f} gallons of gas are needed to drive the {car_choice} {miles} miles.")

