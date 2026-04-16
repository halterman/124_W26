# Initialize counter dictionary
letter_counts = {}
for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letter_counts[ch] = 0

# Open the file for reading
with open('declaration.text', 'r') as f:
    # Read in content of the entire file
    content = f.read()
    # Uppercase the content
    content = content.upper()
    # Count each character A-Z
    for ch in content:
        if 'A' <= ch <= 'Z':
            letter_counts[ch] += 1

    # Report the counts for each letter
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(f'{ch}: {letter_counts[ch]}')

