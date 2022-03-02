employees = {}

while True:
    name = input("Enter employee name: ")
    if name == "$":
        break
    absent_days = int(input("Enter number of absent days: "))
    employees[name] = absent_days

#sort employees by number of absent days
sorted_employees = sorted(employees.items(), key=lambda x: x[1])

for employee in sorted_employees:
    print(employee[0], employee[1])