class StudentScores:

    def __init__(self, scores):
        self.scores = scores

    def _highest_last_two(self):
        try:
            # If less then 2 scores, manually raise error
            if len(self.scores) < 2:
                raise ValueError("Not enough scores to calculate highest of last two.")
            
            # Get last two scores using negative indexing
            last_two = self.scores[-2:]

            # Find highest score
            highest = max(last_two)

            print("Highest of last two scores:", highest)

        except ValueError:
            print("Not enough scores to calculate highest value.")

# MAin Program
try:
    # Take input from user
    user_input = input("Enter the scores: ")

    # Convert input string into list of integers
    score_list = [int(score.strip()) for score in user_input.split(",")]

    # Create object
    student = StudentScores(score_list)

    # Call method
    student._highest_last_two()

except ValueError:
    print("invalid input. Please enter numbers only.")