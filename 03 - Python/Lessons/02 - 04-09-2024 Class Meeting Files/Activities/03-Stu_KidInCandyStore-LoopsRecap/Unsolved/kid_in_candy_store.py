# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []
"""
Create a loop that prints all of the candies in the store to the terminal, with their index sotred in vrackets beside them.

For example: "[0] Snickers
"""
# Print out options
for candy in candy_list:
    #print(candy)
    # to access the index of a candy while looping  through a list, 
    # use list.index(value) function
        # where list = the mname of the list (candy_list)
        # and value = loop control variable (candy)
    print(f"{candy_list.index(candy)} {candy}")

"""
Create a second loop that runs for a set number of times determined by the variable allowance.

For example"""

print(f"Which candies do you want? ")

# set up the loop to run based on the value of allowance
for value in range(allowance):
    # get the choice of candy from the user
    choice = int(input("Enter the number of the candy that you want: "))
    
    # validate the choice of candy from the user
    # len() tell the number of value that are in a list +1, you can use ( - 1) after to make it accurate
    while choice < 0 or choice > (len(candy_list) - 1):
        # display an error and get another input
        choice = int(input("\nINvalid Choice. Enter the number of the candy that you want: "))
    # add the candy from a valid choice to the candy cart
        # use the .append() function to add the candy to the candy cart
        # based on the index from the candy list
    candy_cart.append(candy_list[choice])
    print(f"{candy_list[choice]} was added to the candy cart! \n")


#set up a loop that is baded on a condition as opposed to an allowance
moreCandy = "yes" # varaible allows for us to repeat the loop below
while moreCandy == "yes":
    # get inputs of the candy

    # ask the user if they want more
    moreCandy = input("Do you want more candy? (Enter 'yes' for more, anything else to stop)")
# display the candies from the candy_cart
print("--------------------------")
print("My Candy Cart! \n")
for candy in candy_cart:
    print(candy)