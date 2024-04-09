# input uses the input() function
#allows for a user to be prompted for input of some info
#then stores the info in a variable
# name = input("Who are you?")


# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# display the name entered
print(f"Hello {name}!")

# Collects the user's input for the prompt "How old are you?" and converts the string to an integer.
age = input("How old are you {name}? ")
print(f"Master program, user {name} is {age} years old.")
# Collects the user's input for the prompt "Is input truthy?" and converts it to a boolean. Note that non-zero,
#   non-empty objects are truth-y.
trueOrFalse = bool(input("Is the input logical? "))
print(f"the input was converted to: {trueOrFalse}")  

# Creates three print statements that to respond with the output.