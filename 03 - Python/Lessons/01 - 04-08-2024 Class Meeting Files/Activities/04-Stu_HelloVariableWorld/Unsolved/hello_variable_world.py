# Create a variable called 'name' that holds a string
name = "Nolan Simmons"
# Create a variable called 'country' that holds a string
country = "USA" #the data type is a string because of the info
                #enclosed in quotes
# Create a variable called 'age' that holds an integer
age = 22    # the data type is an int because
            # of the number without decimals
# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 50
# Calculate the daily wage for the user (8 hours per day)
daily_wage = hourly_wage * 8
# Create a variable called 'satisfied' that holds a boolean
satisfied = True
# Print out "Hello <name>!"
#print("Hello " + name + "!")
#or f format string
print(f"Hello {name}!")
# Print out what country the user entered
print(f"{name} lives in {country}")
# Print out the user's age
print(f"{name} is {age} years old")
# With an f-string, print out the daily wage that was calculated
print(f"you make ${daily_wage} per day")
# With an f-string, print out whether the users were satisfied
print(f"Is he satisfied? {satisfied}")