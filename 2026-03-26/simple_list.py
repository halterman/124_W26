x = [10, 20, 30]
print(x)
print([100, 20, 30])

print('--------------')
x = [10, 20, 30]
for i in range(3):
    print(x[i], end=' ')
print()

for i in range(0, len(x), 2):
    print(x[i], end=' ')
print()

for elem in x:
    print(elem, end=' ')
print()