import csv

employeedata = open('EmployeePay.csv', 'r')

csv_file = csv.reader(employeedata)
next(csv_file)

bonus = 0
pay = 0

for rec in csv_file:
    print("first name:", rec[1])
    print("last name:", rec[2])
    salary = float(rec[3])
    print(f"Salary: $ {salary:10,.2f}")
    bonus = salary*float(rec[4])
    print(f"Bonus:  $ {bonus:10,.2f}")
    pay = bonus + salary
    print(f"Pay:    $ {pay:10,.2f}")
    input()