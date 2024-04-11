# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# use a while loop to track while we are still shopping
while shopping.lower() == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")
    
    # get the input of the pie choice
    pieChoice = int(input("Which pie would you like? "))

    # validate the input of the pie choice
        # len(pie_list) = 10 since there are 10 pies in the list
    while pieChoice < 1 or pieChoice > len(pie_list):
        # display an error and ask for an input of a pie number
        pieChoice = int(input("\nInvalid CHoice. Which pie would you like? "))
    # add the pie to the pie list based on the index chosen = pie choice - 1
    pie_purchases.append(pie_list[pieChoice - 1])

    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[int(pieChoice) - 1] + " right out for you.")

    # ask the user if they would like to continue shopping
    shopping = input("Enter 'y' to continue shopping, anything else to stop:")

print(f"Thanks for shopping at 'House of Pies'! Here's your purchase order! {len(pie_purchases)} pies ordered!")
for pie in pie_purchases:
        print(pie)
