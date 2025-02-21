# Created by Andrew Gibbons 10-23-24

# Define quiz_question function with ask and answer as parameters
def quiz_question(ask, answer, correct):
    # Print a statement that this is the quiz_question function
    print('This is the quiz_question function.')
    # Print the ask argument from the main function
    print(ask)
    # Ask for input from the person asking what the answer is
    person_answer = input('What is the answer? ')
    # If the answer argument from main is equal to what the person input for an answer print a correct message
    if answer == person_answer:
        print('Correct!')
    # Else print an incorrect message
    else:
        print('Incorrect.  The correct answer is ' + correct + '')
        # Print a statement that this is the end of the quiz_question function
        print('This is the end of the quiz_question function.')

# Define the main function
def main():
    # For the two_questions function in range of 1 - call quiz_question function twice
    for two_questions in range(1):
        # Print this is the main function
        print('This is the main function.')
        # quiz_question called here has ask, answer, and correct arguments passed to the quiz_question function
        quiz_question('Who composed Jupiter Symphony?', 'Mozart', 'Mozart.')
        quiz_question('What color is an orange? ', 'Orange', 'Orange.')
        # Print this is the end of the main function
        print('This is the end of the main function.')

# Print this is the start of the program
print('This is the start of the program.')

# Call main function
main()

# Print this is the end of the program
print('This is the end of the program.')
