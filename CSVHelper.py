import csv

# Returns key value table strucured by csv columns
def readFile(csvfile, delimiter=';'):
    header = []
    table = []
    with open(csvfile, 'rb') as file:
        rowcounter = 0

        # Read csv file using delimiter. ';' default delimiter
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            if (rowcounter == 0):

                header = row  # stores header array

            # check is table row is a valid row (same lenght of header)
            elif (rowcounter > 0 and len(row) == len(header)):

                # Creates a dictionary for every row
                tablerow = {}
                for index, item in enumerate(row):
                    tablerow[header[index]] = item

                # Appends rows to table array
                table.append(tablerow)

            rowcounter += 1
        return table
