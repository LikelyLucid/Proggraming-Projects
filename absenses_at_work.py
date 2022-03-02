employees = {}

while True:
    name = input("Enter employee name: ")
    if name == "$":
        break
    absent_days = int(input("Enter number of absent days: "))
    employees[name] = absent_days

"""
1. The average number of days of absence per year

2. The name of the person who had the most days of absence

3. An alphabetical list of the names of the people who were not absent at all during the year

4. The names of the people whose period of absence was above the average for the year. (This could be an alphabetical list or a list sorted in descending order of days of absence)"""