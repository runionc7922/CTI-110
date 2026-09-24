# Colin Runion
# 9/24/2026
# P2HW1
# Assignment assess student ability to edit and enhance exiting programs

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
# Get accommodation money from user in the form of an int
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()
# Get food money from user in the form of an int
food = int(input("Last, how much do you need for food? "))
print()
# Display Output, Give all strings the same width formatting and the variables will line up nicely
print("------------Travel Expenses------------")
print(f"{'Location: ':<25}{travel_destination:<25}")
print(f"{'Initial Budget: ':<25}${budget:<25,.2f}")
print(f"{'Fuel: ':<25}${gas:<25,.2f}")
print(f"{'Accommodation: ':<25}${accommodation:<25,.2f}")
print(f"{'Food: ':<25}${food:<25,.2f}")
print("---------------------------------------")
print()
# Add expenses
total_expenses = gas + accommodation + food
# Subtract expenses from budget
print(f"{'Remaining Balance: ':<25}${budget - total_expenses:<25,.2f}")