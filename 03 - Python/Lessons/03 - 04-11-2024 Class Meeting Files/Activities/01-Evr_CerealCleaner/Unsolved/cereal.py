import os
import csv

#cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")

# goes to the path '../Resources/cereal.csv
cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# use the with open() command to read the csv file
with open(cereal_csv) as csvFile:
    # make an instance of the csv reader by using csv.reader() with the ','
    # as a delimiter
    csvReader = csv.reader(csvFile, delimiter=",")

    # read and skip the first row by using th next() command
        # only use when your csv file has a header row
    csvHeader = next(csvFile)

    # read through th e rest of the rows using a loop
    for row in csvReader:
        # Read throug hthe remaining rows and find the cereals that contain five grams of fiber or more, printing the data from those rows to the terminal.
        # name is in index 0
        # grams of fiber is in index 7
        if float(row[7]) >= 5:
            print(row[0]) # print the name of the cereal

        