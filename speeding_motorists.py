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

def check_total_speed(speed_limit, speed):
    if speed < 10:
        fine = 30
    elif speed < 15:
        fine = 80
    elif speed < 20:
        fine = 120
    elif speed < 25:
        fine = 170
    elif speed < 30:
        fine = 230
    elif speed < 35:
        fine = 300
    elif speed < 40:
        fine = 400
    elif speed < 45:
        fine = 510
    else:
        fine = 630
    return fine