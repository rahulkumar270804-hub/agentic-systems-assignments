class StudentMarks:

    def __init__(self, marks):
        
        self.marks = marks  # store the list of marks as an instance variable

    def last_three_average(self):
        # check if there are at least 3 marks
        if len(self.marks) <3:
            print("Not enough marks to calculate average.")
        else:
            #Get last three marks using negative indexing
            last_three_marks = self.marks[-3:]

            #calculate average
            average = sum(last_three_marks) / 3

            print("Average of last 3 marks:", average)
        
            
      
try:
    # Take input from user
    user_input = input("Enter the marks: ")

    # conver input string into list of integer
    mark_list = [int(marks.strip()) for marks in user_input.split(",")]

    # create object 
    student = StudentMarks(mark_list)

    # Call method
    student.last_three_average()

except ValueError:
    print("Invalid input. Please enter marks as integers separated by commas.")
