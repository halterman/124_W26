num1 = int(input())
num2 = int(input())

# Compute the least common multiple of num1 and num2
multiple1 = num1
multiple2 = num2
while multiple1 != multiple2:
    while multiple1 < multiple2:
        multiple1 += num1
    while multiple2 < multiple1:
        multiple2 += num2
print(multiple1)


