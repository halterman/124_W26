

class Point:

    def __init__(self, x: float, y: float) -> None:
        print('Initializing a point object')
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def distance(self, other: Point) -> float: 
        """ Computes the distance between this point and another point. """
        import math
        return math.sqrt((other.x - self.x)*(other.x - self.x) + (other.y - self.y)*(other.y - self.y))


if __name__ == '__main__':
    p1 = Point(10.5, 6)
    print('------------------')
    print(f'p1 = {p1}, its x value is {p1.x}')
    origin = Point(0, 0)
    print(f'origin = {origin}')

