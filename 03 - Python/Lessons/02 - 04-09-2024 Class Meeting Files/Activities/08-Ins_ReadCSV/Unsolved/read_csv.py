"""
# use a path reference
csvPath = '../Resources/contacts.csv'

# use with open() method
with open(csvPath, 'r') as fileHandler:
    # use .read() to read the file into a variable
    lines = fileHandler.read()
    print(lines)
"""
# to handle file paths across your Operating System, use the os module
import os # allows for us to use os.path.join()

# module that allows for us to handle and parse csv files
import csv

# use a path reference using os.path.join()
csvPath = os.path.join("..","Resources", "contacts.csv")
# same as csvPath = '../Resources/contacts.csv'

#use the with open() method to open the file
with open(csvPath) as csvFile:
    # use the csv.reader() function to break everything up baded on the commas
    csvReader = csv.reader(csvFile, delimiter=",")

    # this creates a list of lists that corrresopnd to each row in the file
    for row in csvReader:
        #print(row) # print the list of data briken up by commas on each row of the file

 # index 0 - first names
        # index 1 - last names
        # index 2 - phone numbers
        print(row[0])
        print(row[1])
        print(row[2])
        print("--------------")