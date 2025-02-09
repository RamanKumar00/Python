def average(*numbers):
    sum = 0  # Initialize sum
    for i in numbers:  # Loop through the numbers
        sum += i
    print("Average is:", sum / len(numbers))  # Calculate and print average

# Function call
average(5, 6, 1)
