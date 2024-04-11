# Print Hello User!
print("Hello User!")

# Take in User Input
name = input("What is your name? ")

# Respond Back with User Input
print(f"Hello {name}!")

# Take in the User Favorite Number (42)
favoriteNumber = int(input("What is your favorite number? "))
# Respond Back with a statement based on your favorite number
if favoriteNumber == 42:
    # the number is equal to Nolan's favorite number
    print("Your favorite number is the same as Nolan's")
elif favoriteNumber > 42:
    # the number is greater than Nolan's favorite number
    print("Your favorite number is greater than Nolan's")
else:
    # the number is less than Nolan's number
    print("Your favorite number is less than Nolan.")