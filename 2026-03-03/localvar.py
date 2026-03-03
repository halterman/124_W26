
def sum(x: int) -> int:
    """ Returns the sum of the integers from 
    1 to x, inclusive. """
    s = 0
    for i in range(1, x + 1):
        s += i
    x = 99
    return s

z = 10
print(f'A: z = {z}')
print(sum(10))
print(f'B: z = {z}')



