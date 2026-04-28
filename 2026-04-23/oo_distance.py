from __future__ import annotations

import math
from point import Point



# def distance(p1: Point, p2: Point) -> float:
#     """ Computes the distance between the points (x1,y1) and (x2,y2),
#         where x1, y1, x2, and y2 are numbers. """
#     x1 = p1.x
#     y1 = p1.y
#     x2 = p2.x
#     y2 = p2.y
#     return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

def distance(p1: Point, p2: Point) -> float:
    """ Computes the distance between the points (x1,y1) and (x2,y2),
        where x1, y1, x2, and y2 are numbers. """
    return math.sqrt((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y))

if __name__ == '__main__':
    pt1 = Point(0, 0)
    pt2 = Point(1, 1)
    print(pt1)
    print(pt2)
    dist1 = distance(pt1, pt2)
    dist2 = pt1.distance(pt2) 
    print(f'1. The distance between {pt1} and {pt2} is {dist1}')
    print(f'2. The distance between {pt1} and {pt2} is {dist2}')