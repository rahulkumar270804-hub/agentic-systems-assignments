# Take input from user
try:

    a = input("Enter first number:")
    b = input("Enter Second number:")

# Convert to integers
    a = int(a)
    b = int(b)  

# Print sum
    print("Sum:", a + b)

# Print division result
    print("Division:", a / b)

except ValueError:
    print("invalid input")

except ZeroDivisionError:
    print("cannot divide by zero")
