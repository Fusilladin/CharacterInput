#CHARACTER INPUT

# Create a program that asks the user to enter their name and their age.

name = input("What is your first name?  ")
age = int(input("What is your age?  "))

# Print out a message addressed to them that tells them the year that they will turn 100 years old.

print("Hello, {} you will turn 100 years old in the year {}.".format(name, 2021+100 - age))

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
