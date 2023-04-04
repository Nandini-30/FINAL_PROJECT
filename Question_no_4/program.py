# Defining the size of the hexagon
size = 4

# Define the number of spaces to add before each line of asterisks
spaces = size - 1

# Print the top half of the hexagon
for i in range(size):
    print(' ' * spaces, end='')
    print('* ' * (i + 1))
    spaces -= 1

# Print the bottom half of the hexagon
spaces = 1
for i in range(size - 1):
    print(' ' * spaces, end='')
    print('* ' * (size - i - 1))
    spaces += 1
