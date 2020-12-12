def printETicketNumber(first_name, string):
    e_ticket_number = "".join([first_name[i] + string[i] for i in range(len(first_name))]) + string[len(first_name):]
    return e_ticket_number

def rowandSeat(row, seat):
    rowSeat = "Row: " + row + ", Seat: " + seat
    return rowSeat

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