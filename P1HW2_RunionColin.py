# Colin Runion
# 9/10/2026
# Basic Math On Numbers That Are Entered

print("This program calculates and displays travel expenses.")
print()
# Get budget from user in the form of an int
budget = int(input("Enter Budget: "))
print()
# Get travel destination from user
travel_destination = input("Enter your travel destination: ")
print()
# Get gas money from user in the form of an int
gas = int(input("How much do you think you will spend on gas? "))
print()
# Get accomodation money from user in the form of an int
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
# Get food money from user in the form of an int
food = int(input("Last, how much do you need for food? "))
print()
# Display Output
print("------- Travel Expenses -------")
print("Location: ", travel_destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", accomodation)
print("Food: ", food)
print()
# Add expenses
total_expenses = gas + accomodation + food
# Subtract expenses from budget
print("Remaining Balance: ", budget - total_expenses)