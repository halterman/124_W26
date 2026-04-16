# Initialize counter dictionary
word_counts: dict[str, int] = {}

# Open the file for reading
with open('declaration.text', 'r') as f:
    # Read in content of the entire file
    content = f.read()
    # Uppercase the content
    content = content.upper()
    # Split into words
    words = content.strip().split()
    # Count each word
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1   # Add count for new word
        else:
            word_counts[word] += 1  # Increment existing count

    # Report the counts for each letter
    for word, count in reversed(sorted(word_counts.items())):
        print(f'{word}: {word_counts[word]}')

