import csv
import os

# say that we have three lists
indexes = [1, 2, 3]
names = ["Jim", "James", "Paul"]
departments = ["HR gross", "Sales", "Marketing"]

# we can take our related data and zip it together so that we have rows of the following:
    # each row has an index, name and department
        # ex: [1, "Jim", "HR"]
# use the zop function to zip everyhing together into a list of tuples
staff = list(zip(indexes, names, departments))

# display the contents of each row in the list
for staffMembersRow in staff:
        print(staffMembersRow)

# by using tuples, we can write multiple rows of data at once to a file
outputFile = os.path.join("output.csv") # saves the file in the same folder as .py

# open the output file in write mode
    # newline handles the extra spaces between rows
with open(outputFile, "w", newline='') as csvFile:
        
    # set up the csv.writer with the "," delimiter
    writer = csv.writer(csvFile, delimiter=",")
    
    # call writerow() to write a header for the file
    writer.writerow(["Index", "Name", "Department"])

    # use writerows() to write the data from the list of tuples to the file
    writer.writerow(staff)