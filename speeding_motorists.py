"""
fines:
< 10 km/h = $30

10 - 14 km/h = $80

15 - 19 km/h = $120

20 - 24 km/h = $170

25 - 29 km/h = $230

30 - 34 km/h = $300

35 - 39 km/h = $400

40 - 44 km/h = $510

>= 45 km/h = $630
"""
criminals = ["James Wilson", "Helga Norman", "Zachary Conroy"]

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