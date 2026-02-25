class StudentPerformance:

    def __init__(self, scores):
        self.scores = scores

    def scores_difference(self):
        try:
            # Check if there are at least 2 scores using Indexing
            first_score = self.scores[0]
            last_score = self.scores[-1]

            difference = last_score -first_score

            print("Difference betwen first and last score is:", difference)

        except IndexError:
            print("No score available to calculate difference.")


try:
    # Take input from user
    user_input = input("Enter the scores: ")

    # Convert input string into list of integers
    score_list = [int(score.strip()) for score in user_input.split(",")]

    # Create object
    student = StudentPerformance(score_list)

    # Call method
    student.scores_difference()
    
except ValueError:
    print("Invalid input. Please enter numbers only.")