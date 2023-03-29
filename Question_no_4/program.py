size=int(input("Enter a size for the hexagon:"))

#validate input
if size.digit():
    print("invalid input. Please enter a positive integer.")
    exit()

size=int(size)

#print the hexagon
for i in range(1,2*size):
    if i<=size:
        print(""*(size-i)+"*"*1)

    else:
        print(""*(i-size)+"*"*(2*size-i))
    
        