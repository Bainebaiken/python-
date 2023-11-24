#average of two numbers 
def calculate_average(x, y):
    # Calculate the average
    average = (x + y) / 2
    return average

# Test the function with two numbers
No_1 = 20
No_2 = 40
result = calculate_average(No_2, No_2)

print(f"The average of {No_2} and {No_2} is: {result}")

#program that asks the user to input 3 numbers ,find minimum number test your program by entering 3 different numbers
No_1 = float(input("Enter the first number: "))
No_2 = float(input("Enter the second number: "))
No_3 = float(input("Enter the third number: "))

# Find the minimum number
minimum_number = min(No_1,No_2 ,No_3)

# Display the minimum number
print(f"The minimum number is: {minimum_number}")






