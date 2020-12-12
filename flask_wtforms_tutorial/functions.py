import numpy as np

def printETicketNumber(first_name, string):
    e_ticket_number = "".join([first_name[i] + string[i] for i in range(len(first_name))]) + string[len(first_name):]
    return e_ticket_number

def rowandSeat(row, seat):
    rowSeat = "Row: " + row + ", Seat: " + seat
    return rowSeat

def populateChart():
    chart = np.array([['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O']])
    file = open("reservation.txt", "r")
    for line in file:
        data = line.split(",")
        row = int(data[1])
        seat = int(data[2])
        chart[row][seat] = 'X'
    file.close()
    return chart

def checkSeat(row, seat):
    row = int(row)
    seat = int(seat)
    chart = populateChart()
    if (chart[row][seat] == 'X'):
        return 1
    else:
        return 0

def getTotalRevenue():
    flightSeating = populateChart()
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    totalCost = 0

    for x in range(4):
        for y in range(12):
            if flightSeating[y][x] == "X":
                totalCost += cost_matrix[y][x]        
                
    return totalCost

def checkCreds(username,password):
    file = open("passcodes.txt", "r")

    for line in file:
        data = line.split(",")
        realUser = data[0]
        realPass = data[0]
        if realUser == username and realPass == password:
            file.close()
            return 1
    file.close()
    return 0
    

# def printFlightMap(flight, row, col):
#     for x in col:
#         for y in col:
#             print(flight[x][y])
#             print("\n")
#             return flight[x][y]

# def getTotalRevenue(flightSeating):
#     cost_matrix = [[100, 75, 50, 100] for row in range(12)]
#     totalCost = 0

#     for x in range(4):
#         for y in range(12):
#             if flightSeating[y][x] == "X":
#                 totalCost += cost_matrix[y][x]
#         return totalCost
