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
figuretitle = "test"
unitofmeasure = "t"
delimiter = None

# Check if first argument passed as csv file
if sys.argv[1:] and sys.argv[1].endswith(".csv") and sys.argv[2:] and sys.argv[3:]:
    csvfile = sys.argv[1]  # Storing reference to CSV file
    xaxis = sys.argv[2]
    yaxis = sys.argv[3]
    print("Csv detected")
else:
    # Usage description
    print(bcolors.HEADER +\
        "\nPlease specify csv file path"\
        + bcolors.OKBLUE +\
        "\n\nUSAGE:\npython script.py [PATH OF .csv FILE] [x Axis] [y Axis]"\
        + bcolors.ENDC)
    sys.exit(1)



# Creating result log folder
dirname = os.path.dirname(csvfile)

print(bcolors.OKBLUE + "Reading csv..." + bcolors.ENDC)

# Opens CSV and stores data into a table
csvtable = CSVHelper.readFile(csvfile)

print(bcolors.OKBLUE + "Generating plots for" + csvfile + "..." + bcolors.ENDC)

# Plot using PlotHelper
# plotcsvmetric(csvtable, xaxis, parameter, figuretitle, unitofmeasure)
PlotHelper.plotcsvmetric(csvtable, xaxis, yaxis, figuretitle, unitofmeasure)

# Plot RSRP
print(bcolors.OKGREEN + "\nPNG Graph saved in " + dirname + bcolors.ENDC)