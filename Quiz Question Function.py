# Created by Andrew Gibbons 10-19-24

def quiz_question(ask, answer):
    print('This is the quiz_question function.')
    print(ask)
    person_answer = input('What is the answer? ')
    if answer == 'Mozart':
        print('Correct!')
    else:
        print('Incorrect')
    person_answer = input('What is the answer? ')
    if answer == 'Orange':
        print('Correct!')
    else:
        print('Incorrect')
    person_answer = input('What is the answer? ')
    if answer == 'Neal Armstrong':
        print('Correct!')
    else:
        print('Incorrect')
    print('This is the end of the quiz_question function.')

def main():
    print('This is the main function.')
    quiz_question('Who composed Jupiter Symphony?', 'Mozart')
    quiz_question('What color is an orange? ', 'Orange')
    quiz_question('Who was the first person on the moon? ', 'Neal Armstrong')
    print('This is the end of the main function.')

print('This is the start of the program.')
main()
print('This is the end of the program.')




