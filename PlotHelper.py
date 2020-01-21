#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np


def plotcsvmetric(csvtable, xaxis, parameter, figuretitle, unitofmeasure):
    # Plots the paramter variation in domain specified by timeaxis
    # Calculates average
    # Saves plot as .png file

    # Define figure
    fig, ax = plt.subplots(figsize=(7, 3))

    # Build data array for selected parameter
    dataarray = []
    xarray = []

    for row in csvtable:
        data = float(row[parameter])
        xvalue = float(row[xaxis])
        dataarray.append(data)
        xarray.append(xvalue)

    # Calculating average
    # average = np.average(dataarray)

    # Plot, labeling and options
    ax.plot(xarray, dataarray)
    ax.set(xlabel=xaxis, ylabel=unitofmeasure, title = figuretitle)
    # ax.set_ylim([0, 2]) # uncomment to set y visualization range
    ax.grid()

    # Saving PNG
    fig.savefig(figuretitle + ".png")

    # Show figure
    plt.show()