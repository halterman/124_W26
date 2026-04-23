import math


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """ Computes the distance between the points (x1,y1) and (x2,y2),
        where x1, y1, x2, and y2 are numbers. """
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))


def distance(p1: Point, p2: Point) -> float:
    """ Computes the distance between the points (x1,y1) and (x2,y2),
        where x1, y1, x2, and y2 are numbers. """
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

