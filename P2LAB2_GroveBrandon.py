# Brandon Grove
# 10/2/2026
# P2LAB2
# code that uses a dictionary to store user input and displays output to the user.

cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

#Getting keys from the dictionary
cars_keys = cars.keys()

print(cars_keys)
print(*cars_keys, sep= ", ")

#Get a car from the user
car_name = input("Enter a vehicle to see it's mpg: ")
#get mpg for the car name given
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} mpg.")

#get miles driven from the user
miles_driven = float(input(f"How many miles will you drive with the {car_name}? "))

#calculate the gallons of gas used
gallons_needed = miles_driven / car_mpg

#display results to the user
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")


