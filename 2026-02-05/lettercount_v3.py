# Count the number of letters the user provides,
# except for Z
letter = 'A'
count = 0
while True:
    letter = input()
    if letter == 'Z' or letter == 'z':
        break
    count += 1
print(f'You entered {count} non-Z letters')