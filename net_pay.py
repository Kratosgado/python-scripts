#This is a program to calculate the net income of a worker at a particular firm

'''
QUESTION

Employees of a certain firm are paid on hourly basis.
If an employee works for not more than 40 hours a week, the hours worked is considered regular
and overtime for hours worked beyond 40. Regular hours are paid at per hour while the overtime
rate is one and half times the regular rate per hour. All employees are to pay 15% of their gross
pay as Income Tax, 2.5% as National Health Contribution Levy, 1% as District Tax. Employees who
have more than three children are to pay 50 pesewas per child in excess of three towards Educational
Fund for all

Devise a computer solution that can be used to calculate deductions as well as the Net Pay of 
emoloyees
'''

#outputs = deductions made, net pay
#regular hours = 5cedis per hour
#overtime hours, after 40 hours = 1.5 times 5 per hour

#deductins: Income tax = 15% , NHCL = 2.5% , District Tax = 1% , Edu fund = 50ps per each excess child

#get inputs : hours worked, number of children
hrs_worked = int(input('How many hours did you work : '))
num_chd = int(input('Number of children : '))

#calculate overtime if any
overtime = hrs_worked - 40

#calculate the regular pay
reg_pay = hrs_worked * 5

#check if there's overtime and calculate its pay
if overtime > 0:
    ot_pay = overtime * 7.5
    gross_pay = reg_pay + ot_pay
else:
    gross_pay = reg_pay

#check deductions and print them out
inc_tax = (15/100) * gross_pay
nhcl = (2.5/100) * gross_pay
dis_tax = (1/100) * gross_pay
print(f' You were deducted;\n {inc_tax} as income tax\n {nhcl} as National Health Contribution Levy\n {dis_tax} as District Tax')

if num_chd > 3:
    edu_fund = (num_chd - 3) * 0.5
    print(f'You were deducted {edu_fund} for Educational Fund For All ')
else:
    edu_fund = 0
    print('You didnt pay anything for Educational Fund For All')

net_pay = gross_pay - (inc_tax + nhcl + dis_tax + edu_fund)
print(f'Your net pay for the week is {net_pay}')
