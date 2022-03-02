employees = {}

while True:
    name = input("Enter employee name: ")
    if name == "$":
        break
    absent_days = int(input("Enter number of absent days: "))
    employees[name] = absent_days

#sort employees into alphabetical order
e