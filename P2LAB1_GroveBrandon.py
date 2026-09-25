# Brandon Grove
# 9/24/2026
# P2LAB1
# Inputing numbers to be calculated and displayed

#Import math module to use the constant, math.pi
import math

# User given radius
radius = float(input("What is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius

# Display diamter
print(f"The diameter of the circle is {diameter:.1f}\n")

# calculate circumfrence
circumfrence = 2 * math.pi * radius

# Display circumfrence 
print(f"The circumfrence of the circle is {circumfrence:.2f}\n")

# The area calculation
circle_area = math.pi * radius ** 2

# Display area
print(f"The area of the circle is {circle_area:.3f}\n")


