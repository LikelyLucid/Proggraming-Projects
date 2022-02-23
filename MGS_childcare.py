"""
You are to design and write a program that will be used by a child day-care centre. It will keep track of children throughout the day. There will be many features in the program, but we will take it a step at a time and build each one in turn.
"""

HOURLEY_COST = 12
children = []


def dropOff():
    print("Drop off a child")
    print("Please enter the following details")
    print()
    name = input("Name: ").capitalize()
    children.append(name) # add {name} to the roll
    print(f"{name} has been added to roll")


def pickUp():
    print("Pick up a child")
    print("Please enter the following details")
    print()
    
    try:
        name = input("Name: ").capitalize()
        children.remove(name)
        print(f"{name} has been removed from roll")

    except ValueError:
        print("Child not found")


def calcCost():
    hours = int(input("Hours: "))
    cost = hours * HOURLEY_COST * len(children)
    print("Cost: $" + str(cost))


def printRoll():
    print("Printing roll\n")
    for child in children:
        print(child)


choice = 0
while choice != 5:
    print("-------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropOff()

    elif choice == 2:
        pickUp()

    elif choice == 3:
        calcCost()

    elif choice == 4:
        printRoll()

    elif choice == 5:
        print("Goodbye")

    else:
        print("Invalid choice")
        print()
