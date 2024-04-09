"""
	In VB we learned about Arrays
    
    Example:
        Dim Ghost(4) As String - made an array of strings
        Ghosts(0) = "Inky"
        Ghosts(1) = "Blinky"
        Ghosts(2) = "Pinky"
        Ghosts(3) = "Clyde"
        
    In python, we have lists and tuples
        ghosts = ["inky", "BLinky", "Pinky", "Clyde"] - items can be changed
        ghosts01 = ("Inky", "Blinky", "Pinky", "Clyde") - items can't be changed
"""
#ghosts = ["Inky", "Blinky", "Pinky", "Clyde"]
ghosts = ["Inky", "Blinky", "Pinky", "Clyde"]

# or the data can be mixed
data = ["A", 1, "one", "AYE"]

#display the information in both lists
print(ghosts)
print(data)

# print an index of a place of information in each list
print(ghosts.index("Clyde")) # searches for the data in the lists
                             #and returns the index
print(data.index(1))

#change the value of data in an index
ghosts[3] = "Sue" # changes 'CLyde' to 'Sue'
data[2] = "two" # changes 'one' to 'two'

# display the updated information in both lists
print(ghosts)
print(data)

# add an item to a lists
ghosts.append("Clyde")

#remove an item from a list
#remove() removes an item based on value
data.remove("AYE")
# use pop() to remove an item based on index value
data.pop(0) # removes the item in index 0

# display the updated information
print(ghosts)
print(data)