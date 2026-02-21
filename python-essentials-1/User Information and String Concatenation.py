try:
    # Take Input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")

    # Convert age into integer
    age = int(age)

    # Check if age is negative
    if age < 0:
        print("Age cannot be negative.")
    else:
        # print full name using concatenation
        full_name = first_name + " " + last_name

        # Print full name and age
        print("Full Name:", full_name)

        # print age next year
        print("You will be  " + str(age + 1) + " next year.")

except ValueError:
    print("Invalid input for age. Please enter a valid number.")
    