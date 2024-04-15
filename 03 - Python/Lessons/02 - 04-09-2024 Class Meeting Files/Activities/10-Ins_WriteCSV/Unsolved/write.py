# Dependencies
import os
import csv

# use os.path.join() to write to ../output/output.csv
outputPath = os.path.join("..", "output", "output.csv")

# open the file using with open() adding the 'w' argument
# to open the file in write mode
with open (outputPath, "w") as csvFile:

    # initialize the csv.writer with the comma as a delimiter
    csvWriter = csv.writer(csvFile, delimiter=",")

    # use writerow() to write data to the file as a list, which
    # will be separated by commas in the file
    csvWriter.writerow(["ghost Name", "Color"]) # wirte a header

    csvWriter.writerow(["Inky", "Blue"]) # wirte a header

    csvWriter.writerow(["Blinky", "Green"]) # wirte a header

    csvWriter.writerow(["Pinky", "Pink"]) # wirte a header

    csvWriter.writerow(["Clyde", "Orange"]) # wirte a header


    