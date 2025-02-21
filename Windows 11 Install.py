# Created by Andrew Gibbons 10-11-24

# To install Windows 11, a computer must have 8GB of memory and 64GB of free storage space, and be running Windows 10.
# (Source, Microsoft)For this program, give me hints but don't write a full solution.
#
# All three requirements must be met.
#
# Write a windows_11_compatible function that takes three arguments, the amount of memory, the free storage space,
# and current operating system.
#
# In the windows_11_compatible function use conditions to figure out if the user's computer can be upgraded to Windows 11 or not.
#
# You'll need to check that the memory is at least 8, the free storage space is at least 64, and the name of the current
# operating system equals 'Windows 10'
#
# Your windows_11_compatible function should return one of the Boolean values True (if the computer can be upgraded) or
# False (if it can't be upgraded).  The can_upgrade function will not print anything.
#
# Create a main function.  In the main function, ask the user for
#
# The current memory in their computer, in GB.  (For example, a user with 8GB of memory would enter 8)
# The amount of free storage space, in GB. (For example, a user with a 500GB of free space should enter 500)
# The name of their current operating system. (For example, a user could enter Windows 10 or Windows 8 or Windows 7
# or Windows XP or Linux or MacOS...)

# Call your windows_11_compatible function from main(), and use the return value to print a message to the user
# telling them if they can, or can't, upgrade.

# Define a function with three parameters relating to memory, storage and operating system
def windows_11_compatible(memory, storage, os):
    # If memory, storage and operating system are the minimum required return True, else return false
    # Check if all conditions are met
    if memory >= 8 and storage >= 64 and os == 'Windows 10':
        return True
    else:
        return False

# Define main function with no parameters
def main():
    # Get user inputs
    memory = int(input("Enter the current memory in your computer (in GB): "))
    storage = int(input("Enter the amount of free storage space (in GB): "))
    os = input("Enter the name of your current operating system: ")

    # As part of main function call windows_11_compatible function and check to see if all three parameters are true and print an
    # upgrade message, else print an ineligible for upgrade message
    # Check compatibility
    if windows_11_compatible(memory, storage, os):
        print("Your computer can be upgraded to Windows 11.")
    else:
        print("Your computer cannot be upgraded to Windows 11.")

# Call main function
main()