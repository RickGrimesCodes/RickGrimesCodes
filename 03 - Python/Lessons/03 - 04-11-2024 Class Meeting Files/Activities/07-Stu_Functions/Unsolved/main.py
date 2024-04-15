# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(values):
    # average = sum / count
    # first, compute the sum of the numbers in the list
    total = 0 # running total
    # loop through each value in the list
    for number in values:
        # add on to the running total
        total += number 
    # second, get the count of the number of items in the list
    count = len(values)
    # third, we calculate and return the average
    avg = total / count
    return avg
# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
