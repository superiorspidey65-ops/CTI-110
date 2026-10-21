# Brandon Grove
# 10/16/2026
# P3LAB
# Calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

amount_money = float(input("Enter the amount of money as a float: $"))

# Convert the amount of money to cents
cents = int(amount_money * 100)

# Calculate the number of dollars, quarters, dimes, nickels, and pennies needed

if cents == 0:
    print("No change.")
    raise SystemExit

dollars = cents // 100
cents = cents - (dollars * 100)

quarters = cents // 25
cents = cents - (quarters * 25)

dimes = cents // 10
cents = cents - (dimes * 10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

# Display the results to the user

if dollars == 1:
    print(f"{dollars} Dollar")
else:
    print(f"{dollars} Dollars")

if quarters == 1:
    print(f"{quarters} Quarter")
else:
    print(f"{quarters} Quarters")

if dimes == 1:
      print(f"{dimes} Dime")
else:
    print(f"{dimes} Dimes")

if nickels == 1:
    print(f"{nickels} Nickel")
else:
    print(f"{nickels} Nickels")

if pennies == 1:
    print(f"{pennies} Penny")
else:
    print(f"{pennies} Pennies")
