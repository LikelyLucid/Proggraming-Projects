criminals = ["James Wilson", "Helga Norman", "Zachary Conroy"]
drivers = {}
def check_total_speed(speed):
    if speed < 10:
        return 30
    elif speed < 15:
        return 80
    elif speed < 20:
        return 120
    elif speed < 25:
        return 170
    elif speed < 30:
        return 230
    elif speed < 35:
        return 300
    elif speed < 40:
        return 400
    elif speed < 45:
        return 510
    else:
        return 630

while True:
    name = input("enter the drivers full name: ")
    