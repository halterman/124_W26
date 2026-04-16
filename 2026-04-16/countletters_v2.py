# Initialize 26 counters
letter_counts = [0 for _ in range(26)]

# Open the file for reading
with open('declaration.text', 'r') as f:
    # Read in content of the entire file
    content = f.read()
    print('---------------')
    print(content)
    # Uppercase the content
    content = content.upper()
    print('###############')
    print(content)
    
    # Count each character A-Z
    for ch in content:
        if 'A' <= ch <= 'Z':
            letter_counts[ord(ch) - ord('A')] += 1

    # Report the counts for each letter
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(f'{ch}: {letter_counts[ord(ch) - ord('A')]}')

