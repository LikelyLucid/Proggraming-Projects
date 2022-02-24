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
while True:
    input