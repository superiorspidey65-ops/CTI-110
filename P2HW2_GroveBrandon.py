# Brandon Grove
# 10/7/2026
# P2HW2
# Write a program that asks the user to enter test grades in modules, list them and display them


# Get user input for grades in each module

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store the grades in a list

grades = [module1, module2, module3, module4, module5, module6]


# Organize Grades from user

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_modules = sum(grades)
average_grade = sum_of_modules / len(grades)

# Format and display the results
print("\n------------Results------------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_of_modules}")
print(f"Average Grade: {average_grade:.2f}")
print("-----------------------------------------")