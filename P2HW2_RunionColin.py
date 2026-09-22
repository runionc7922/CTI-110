# Colin Runion
# 9/22/2026
# P2HW2
# Lists

# Get six inputs from user
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Create a list holding user inputs
module_grades = [module1, module2, module3, module4, module5, module6]

# Use sum function to add all values in the list
sum_of_grades = sum(module_grades)

# Use sum function to get average of all values in the list
average = sum_of_grades / len(module_grades)

# Display Output
print()
print("------- Results -------")
print(f"Lowest Grade: {min(module_grades):.2f}")
print(f"Highest Grade: {max(module_grades):.2f}")
print(f"Sum of Grades: {sum_of_grades:.2f}")
print(f"Average: {average:.2f}")
print("--------------------------------")