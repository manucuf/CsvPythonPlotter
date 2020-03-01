#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np


def plotcsvmetric(csvtable, xaxis, parameter, figuretitle, unitofmeasure, displayaverage):
    # Plots the paramter variation in domain specified by timeaxis
    # Calculates average
    # Saves plot as .png file

    # Define figure
    fig, ax = plt.subplots(figsize=(7, 7))

    # Build data array for selected parameter
    dataarray = []
    xarray = []

    for row in csvtable:
        data = float(row[parameter])
        xvalue = float(row[xaxis])
        dataarray.append(data)
        xarray.append(xvalue)

    # Calculating average
    average = np.average(npdataarray)

    # Plot, labeling and options
    ax.plot(npx, npdataarray)
    if (displayaverage == True):
        ax.set(xlabel=xaxis, ylabel=unitofmeasure, title = figuretitle + '\n\nAverage = ' + str(average))
    else:
        ax.set(xlabel=xaxis, ylabel=unitofmeasure, title = figuretitle)
    ax.grid()

    # Saving PNG
    fig.savefig(figuretitle + ".png")

    # Show figure
    plt.show()