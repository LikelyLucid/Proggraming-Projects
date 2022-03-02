employees = {}

while True:
    name = input("Enter employee name: ")
    if name == "$":
        break
    absent_days = int(input("Enter number of absent days: "))
    employees[name] = absent_days

average_days_off = sum(employees.values()) / len(employees)
print("The average number of days of absence per year is: ", average_days_off)

max_absent_days = max(employees.values())
print("The name of the person who had the most days of absence is: ", max(employees, key=employees.get))

for name, absent_days in employees.items():
    if absent_days == 0:
        print("The name of the person who was not absent at all during the year is: ", name)
names_over_average = [
    name
    for name, absent_days in sorted(employees.items())
    if absent_days > average_days_off
]
