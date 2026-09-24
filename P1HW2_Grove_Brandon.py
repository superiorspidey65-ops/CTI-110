 # Brandon Grove
 # 9/22/2026
 # P1HW2
 # Inputting a travel budget and outputting the amount of money spent and the remaining budget.

print("This program calculates and displays travel expanses")
print()

budget = float(input("Enter budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas = float(input("How much do you think you will spend on gas? "))
print()

accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food?"))
print()

print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()

remaining_budget = budget - (gas + accommodation + food)
print("Remaining Budget:", remaining_budget)
