# Get table size form the user
size = int(input('Please enter table size: '))

# Print the column titles
for column in range(1, size + 1):
    print(f'{column:4}', end='')
print()
for column in range(1, size + 1):
    print('----', end='')
print()

# Print the table
for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f'{row * column:4}', end='')
    print()