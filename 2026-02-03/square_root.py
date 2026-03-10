from math import sqrt

i = float(input())

# Compute square root of i
r = 1.0  # Set provisional root
while r*r - i > 0.00000001 or r*r - i < -0.00000001:
    r = (r + i/r)/2
    print('r is now', r)

print(r)
print(sqrt(i))