# Created by Andrew Gibbons 10-1-24
#
# Start with the greeting program, the first program with functions we used in Python Tutor.
# It's from this video.  Modify the greeting function to return the user's name in uppercase,
# with !!!! after it.  The greeting function should convert the name to uppercase.
#
# Call the greeting function from the main function, and print the
#
# So, if the user's name is Miriam, the greeting function will return 'HELLO MIRIAM!!!!'

# Define greeting function with parameter name
def greeting(name):
    # Print a message to say hello to the input name
    message = f'HELLO {name.upper()}!!!!'
    return message

# Define main function with no parameters
def main():
    # Define variable username and assign the value andrew
    username = 'andrew'
    # Call greeting function with username as argument
    hello_message = greeting(username)
    # Print a hello to the person's name message
    print(hello_message)

main()
