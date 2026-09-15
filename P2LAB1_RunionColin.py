# Colin Runion
# 9/15/2026
# CTI-110
# Calculate components of circle using pi from math library

import math

print(math.pi)

# Get radius from user
radius = float(input("Enter the radius: "))

print()

# Calculate diameter
diameter = 2 * radius

# Display radius using an f-string
print(f"The diameter of the circle is {diameter:.1f}")

# Calculate circumference
circumference = 2 * math.pi * radius

# Display circumference using f-string
print(f"The circumference of the circle is {circumference:.2f}")

# Calculate the area
area = math.pi * math.pow(radius, 2)

# Display area with f-string
print(f"The area of the circle is {area:.3f}")