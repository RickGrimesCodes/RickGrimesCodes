"""
 format of a user-defiend fucntion
 
    def nameOfFunction(parameters):
        # code that runs when the function is called
        return

# functions do not have to have parameters, if you do not want your function to accept / require data to run

# functions do not have to return data
"""
"""
# simple function that displays a message when called
def greeting():
    print("Hello!")


    greeting is the name of the function when the function is called, greeting(), then the message
    'Hello!' is displayed

# call greeting
greeting()
"""
"""
# simple function that takes a parameter and displays a message
# using the parameter
#def greeting(name):
   # print(f"Hello {name}!") # displays the value of the parameter

# simple function that takes a parameter and displays a message
# using the parameter, with a defualt value of "Dr. A"
def greeting(name="Dr, A"):
    print(f"hello {name}!") # displays the value of the parameter
                            # or display Dr. A if no parameter is passed
# call greeting with two different values
greeting("Cindy")
greeting("Nolan")
# call greeting with no parameter, that uses the defualt value
greeting()
"""

""" I REALLY WANT TO AUTOMATE THIS!!!!!!!!!!!!!!!!!!
# function with multiple arguments
def makeSmoothie(numOunces=8, ingredient="strawberries"):
    print(f"You ordered a {numOunces} oz smoothie with {ingredient}.")
    numOunces = 8

makeSmoothie(16, "mangoes")
# call function with one default value
makeSmoothie(,"pineapples")
# call function using default values
makeSmoothie()
"""

# function that returns data
def addOne(num):
    return num+1 # takes the parameter and adds 1 its value and send it back

# declare a variable to hold a number
number = 2
# call on funciton, pass in the number, then return the number and store it in 
# numberPlusOne
numberPlusOne = addOne(number)
print(f"number = {number}")
print(f"numberPlusOne = {numberPlusOne}")