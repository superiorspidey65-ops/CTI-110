# Your Name
# 10/28/2026
# P4LAB2
# Ability to use loops to display information to users.


# get interger from user
# Determine if integer is positive or negative
# if positive, display multiplication table
# if number is negative, tell user it can't be accepted
# ask user to run again

run_again = 'yes'

while run_again.lower() != 'no':
    
    user_input = int(input("Enter an integer: "))
    
    if user_input > 0:
        #display multiplication for the number and range
        for item in range(1, 13):
            print(f"{user_input} * {item} = {user_input * item}")
    else:
        
        print("This program does not handle negative numbers.")
        
    run_again = input("Would you like to run the program again? (yes/no): ")

#Loop has ended, because 'no'
print("Program has ended.")