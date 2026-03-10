<<<<<<< Updated upstream
from math import sqrt

for i in range(10, 20):
    # Compute square root of i
    r = 1.0  # Set provisional root
    while r*r - i > 0.00000001 or r*r - i < -0.00000001:
        r = (r + i/r)/2
    print(f'The square root of {i} is {r} or {sqrt(i)}')
=======
from math import sqrt

for i in range(10, 20):
    # Compute square root of i
    r = 1.0  # Set provisional root
    while r*r - i > 0.00000001 or r*r - i < -0.00000001:
        r = (r + i/r)/2
    print(f'The square root of {i} is {r} or {sqrt(i)}')
>>>>>>> Stashed changes
