# Brandon Grove
# 11/1/2026
# P4HW2
# The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

# employee information
employee = input("Enter employee's name (or 'done' to finish): ")

#Create Accumulator variables for overtime, regular pay, gross pay, and employee count
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while employee != "done":
    #add employee count
    employee_count += 1 # employee_count = employee_count + 1
    # Ask employee information
    hours = float(input("How many hours did " + employee + " work this week? "))
    pay_rate = float(input("What is " + employee + "'s hourly pay rate? "))

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

        #add to accumulators total
    total_overtime_pay += over_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay


    # Display results
    print('----------------------------------------')
    print(f'{"Employee Name:":<2}', employee)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
    print('---------------------------------------------------------------------------------------')
    print(f'{hours:<15.1f}{pay_rate:<12.2f}{over_time:<12.2f}{over_pay:<12.2f}{regular_pay:<15.2f}${gross_pay:<12.2f}')

    employee = input("Enter employee's name (or 'done' to finish): ")

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(total_overtime_pay, ',.2f'))
print("Total amount paid for regular time: $", format(total_regular_pay, ',.2f'))
print("Total amount paid for all employees: $", format(total_gross_pay, ',.2f'))