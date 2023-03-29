num=int(input("Enter a non-negative integer:"))

#check if input is invalid 
if num<0:
    print("Invalid input,Please enter a non-negative integer.")
else:
    #calculate the factorial
    factorial = 1
    for i in range(1,num+1):
        factorial*=i

    #print the result
    print("The factorial of",num,"is",factorial)


