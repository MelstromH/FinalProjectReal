def printFlightMap(flight, row, col):
    for x in col:
        for y in col:
            print(flight[x][y])
            print("\n")
	
	
def getTotalRevenue(flightSeating):

	cost_matrix = [[100, 75, 50, 100] for row in range(12)]
	totalCost = 0

    	for x in range(4):
        	for y in range(12):
				
            		if flightSeating[y][x] == "X":
               	
		totalCost += cost_matrix[y][x]
                
    return totalCost

