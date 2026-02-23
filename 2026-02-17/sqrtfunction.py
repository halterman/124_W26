from math import sqrt

def my_sqrt(x: float) -> float:
    # Compute square root of i
    r = 1.0  # Set provisional root
    while r*r - x > 0.00000001 or r*r - x < -0.00000001:
        r = (r + x/r)/2
    return r

val2 = 18

def count(n: int) -> None:
    val2 = 0
    for val in range(n):
        print(val)
    print(val2)

print(val2)
    
print(my_sqrt(16))
print('----------------------------')

for i in range(10, 20):
    print(f'The square root of {i} is {my_sqrt(i)} or {sqrt(i)}')

print('----------------------------')

count(7)