import numpy as np

def printFlightMap(flight, row, col):
    for x in col:
        for y in col:
            print(flight[x][y])
            print("\n")

chart = np.array([['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O']])

newchart = chart.reshape(12,4)

print(newchart)
