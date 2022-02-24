item = input("What is the auction for? ")
while item.value()
reserve = int(input("What is the reserve price? "))
print(f"The auction for the {item} has started !")
highest_bid = 0
bid = 0

while highest_bid != -1:
    try:
        bid = int(input("what is your bid? "))
    except ValueError:
        print("Please enter an integer")
        bid = highest_bid
    if bid > highest_bid:
        highest_bid = bid
    else:
        print("need a higher bid")
    print(f"highest bid so far is ${highest_bid}")

if highest_bid < reserve:
    print(f"The {item} didn't sell")
else:
    print(f"The {item} sold successfully")