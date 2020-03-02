import math


def firstrun():
    return "success"


def circlearea(radius):
    if radius < 0:
        return "Invalid value for radius"
    area = math.pi * radius**2
    return area


def firstlast(thislist=[], *args):
    if len(thislist) == 0:
        return "The list is empty"
    first = thislist[0]
    last = thislist[-1]
    return first, last
