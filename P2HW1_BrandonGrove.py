# Brandon Grove
# 10/6/2026
# P2HW1
# Adjusted P1HW2 assignment

# Description message
print("This program calculates and displays travel expanses")
print()

# Get travel budget from user
budget = float(input("Enter budget: "))
print()

# Get travel destination from user
destination = input("Enter your travel destination: ")
print()

# Get estimated gas expense from user
gas = float(input("How much do you think you will spend on gas? "))
print()
# Get estimated hotel accommodation expense from user
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

# Get estimated food expense from user
food = float(input("Last, how much do you need for food? "))
print()

# --- Formatted Output Section ---
print("------------Travel Expenses------------")
# Using a width of 18 left-aligned (<18) to match your exact text alignment

print(f"{'Location:':<18}{destination}")
print(f"{'Initial Budget:':<18}${budget:.2f}")
print(f"{'Fuel:':<18}${gas:.2f}")
print(f"{'Accommodation:':<18}${accommodation:.2f}")
print(f"{'Food:':<18}${food:.2f}")
print("----------------------------------------")
print()

# Calculate and display the final balance
remaining_budget = budget - (gas + accommodation + food)
print(f"{'Remaining Budget:':<18}${remaining_budget:.2f}")
