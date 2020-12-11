def printETicketNumber(first_name):
    string ="INFOTC4320"
    e_ticket_number = "".join([first_name[i] + string[i] for i in range(len(first_name))]) + string[len(first_name):]
    print("Hello world!")
    return e_ticket_number
def printFlightMap(flight, row, col):
    for x in col:
        for y in col:
            print(flight[x][y])
            print("\n")