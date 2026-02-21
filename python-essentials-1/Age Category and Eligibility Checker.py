try:
    # Take Input
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # Convert gae to integer
    age = int(age)

    # Check negative age
    if age<0:
        print("Age cannot be negative.")
    else:
        print("Hello: " + name)

    # Age Category
        if age < 13:
            print("You are a child.")
        elif 13 <= age <= 17:
            print("You are a teenager.")
        elif 18 <= age < 59:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")

        # Voting Eligibility
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

except ValueError:
    print("invalid age input")