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
    elif answer == "no":
        print("Thank you for using the taxi system, {}".format(name))
        break
    else:
        print("Please enter yes or no")
total_average_time = sum(average_time) / len(average_time)
total_average_time = round(total_average_time, 2)
# print totals for the day and averages
print("Total time: {} minutes".format(total_time))
print("Average time: {} minutes".format(total_average_time))
print("Total income: ${}".format(total_income))
print("Average income: ${}".format(sum(average_income) / len(average_income)))


