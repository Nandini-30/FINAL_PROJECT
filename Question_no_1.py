temp=float(input("Enter the temperature:"))

convert_to=input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius:")

# Convert the temperature
if convert_to=="C":
    celsius=(temp-32)*5/9
    print(temp,"degrees Fahrenheit is", round(celsius,1),"degrees Celsius.")

elif convert_to=="F":
    fahrenheit=temp*9/5+32
    print(temp,"degrees Celsius is", round(fahrenheit,1),"degrees Fahrenheit.")
else:
    print("Invalid input.Please enter 'C' or 'F'.")