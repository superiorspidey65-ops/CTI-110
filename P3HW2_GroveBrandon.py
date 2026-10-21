# Brandon Grove
# 10/17/2026
# P3HW2
# Calculating a employees name based on their hours worked

# employee information
employee = input('Enter employe name: ')
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# if else statements for overtime
if hours >= 40:

    # Calculating overtime
    over_time = hours - 40

    # Calculating overtime pay
    over_pay = over_time * (pay_rate)

    #regular hours pay
    regular_pay = 40 * pay_rate

    # Calculating Gross pay
    gross_pay = regular_pay + over_pay
else:

    over_pay = 0
    over_time = 0
    regular_pay = hours * pay_rate
    gross_pay = regular_pay


# Display results
print('----------------------------------------')
print(f'{"Employee Name:":<2}', employee)
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
print('---------------------------------------------------------------------------------------')
print(f'{hours:<15.1f}{pay_rate:<12.2f}{over_time:<12.2}{over_pay:<12.2f}{regular_pay:<15.2f}${gross_pay:<12.2f}')

