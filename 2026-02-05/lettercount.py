# Count the number of letters the user provides,
# except for Z
letter = 'A'
count = 0
while letter != 'Z' and letter != 'z':
    letter = input()
    if letter != 'Z' and letter != 'z':
        count += 1
print(f'You entered {count} non-Z letters')