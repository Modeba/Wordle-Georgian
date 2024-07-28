# Get words
with open('dictionary.txt', 'r') as file:
    lines = file.readlines()
    words = []
    for line in lines:
        line = line.strip()
        if len(line) == 5:
            words.append(line)

# Update the file
with open('dictionary.txt', 'w') as file:
    for word in words:
        file.write(f'{word}\n')

input()
