def integer_check(question):
    try:
        return int(input(question))
    except ValueError:
        print("Please enter an integer")
        integer_check(question)


item = input("What is the auction for? ")
reserve = int(input("What is the reserve price? "))
print(f"The auction for the {item} has started !")
highest_bid = 0
bid = 0

while highest_bid != -1:
    bid = int(input("what is your bid? "))
    if bid > highest_bid:
        highest_bid = bid
    else:
        print("need a higher bid")
    print(f"highest bid so far is ${highest_bid}")

if highest_bid < reserve:
    print(f"The {item} didn't sell")
