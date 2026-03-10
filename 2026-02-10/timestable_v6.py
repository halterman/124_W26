# Get table size form the user
size = int(input('Please enter table size: '))

# Print the column titles
print('      ', end='')
for column in range(1, size + 1):
    print(f'{column:4}', end='')
print()
print('      ', end='')
for column in range(1, size + 1):
    print('----', end='')
print()

# Print the table
for row in range(1, size + 1):
    print(f'{row:4} |', end='')
    for column in range(1, size + 1):
        print(f'{row * column:4}', end='')
    print()