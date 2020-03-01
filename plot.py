#!/usr/bin/python
import sys
import os
import shutil

import CSVHelper
import PlotHelper


# Terminal log colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


xaxis = None
yaxis = None
figuretitle = None
unitofmeasure = None
delimiter = None

# Check if first argument passed as csv file
if sys.argv[1:] and sys.argv[1].endswith(".csv") and sys.argv[2:] and sys.argv[3:] and sys.argv[4:] and sys.argv[5:] and sys.argv[6:]:
    csvfile = sys.argv[1]  # Storing reference to CSV file
    xaxis = sys.argv[2]
    yaxis = sys.argv[3]
    figuretitle = sys.argv[4]
    unitofmeasure = sys.argv[5]
    delimiter = sys.argv[6]
    print("Csv detected")
else:
    # Usage description
    print(bcolors.HEADER +\
        "\nPlease specify csv file path"\
        + bcolors.OKBLUE +\
        "\n\nUSAGE:\npython script.py [PATH OF .csv FILE] [x Axis] [y Axis] [title] [unit] [delimiter]"\
        + bcolors.ENDC)
    sys.exit(1)



# Creating result log folder
dirname = os.path.dirname(csvfile)

print("Reading csv...")

# Opens CSV and stores data into a table
csvtable = CSVHelper.readFile(csvfile, delimiter=delimiter)

if len(csvtable) == 0:
    print("An error occurred when loading data")
    sys.exit(1)


print("Generating plots for" + csvfile + "...")

# Plot using PlotHelper
# plotcsvmetric(csvtable, xaxis, parameter, figuretitle, unitofmeasure)
PlotHelper.plotcsvmetric(csvtable, xaxis, yaxis, figuretitle, unitofmeasure, False)

# Plot RSRP
print("\nPNG Graph saved in " + dirname)