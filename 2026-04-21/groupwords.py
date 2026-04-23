groups: dict[int, list[str]] = {} # Initialize grouping dictionary
with open('declaration.text', 'r') as f: # Open file for reading
    # Read in content of the entire file    
    content = f.read() 
    # Make list of individual words
    words = content.split()
    for word in words:
        word = word.upper() # Make the word all caps
        # Compute the word’s length
        size = len(word)
        if size in groups:
            # Avoid duplicates
            if word not in groups[size]:
                # Add the word to its group
                groups[size] += [word]
        else:
            # Add the word to a new group
            groups[size] = [word]
    # Show the groups
    for size, group in sorted(groups.items()):
        print(size, ':', group)