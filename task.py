import math



def firstrun():
    return "success"


def circlearea(radius):
    if radius < 0:
        return "Invalid value for radius"
    area = math.pi * radius**2
    return area