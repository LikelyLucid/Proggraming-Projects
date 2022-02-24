"""
The program should start off by asking for the driver’s name. It should then repeatedly ask to start a new trip.

If the user says "yes", ask for the time the trip took in minutes. It should print out the cost at the end of the trip which is a base cost of $10 plus $2 extra for each minute the trip took.

At the end of the day the user will say "no" to more trips, and the system should print:

● The driver’s name

● Total time of all trips

● Average time of all trips

● Total income for the day

● Average cost of all trip
"""
name = input("What is your name? ")
total_time = 0
average_time = []
total_income = 0
average_income = []

while True:
    answer = input("Would you like to start a trip? ").lower()
    if answer == "yes":
        time = int(input("How many minutes did the trip take? "))
        total_time += time
        average_time.append(time)
        income = 10 + 2 * time
        total_income += income
        average_income.append(income)
    else:
        break

total_average_time = sum(average_time) / len(average_time)
total_
