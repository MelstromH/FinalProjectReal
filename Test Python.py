import numpy as np
def printETicketNumber(first_name, string):
    e_ticket_number = "".join([first_name[i] + string[i] for i in range(len(first_name))]) + string[len(first_name):]
    return e_ticket_number
def printFlightMap(flight, row, col):
    for x in col:
        for y in col:
            print(flight[x][y])
            print("\n")

chart = np.array([['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','O']])

newchart = chart.reshape(12,4)

print(newchart)


first_name = 'Alice'
string = "INFOTC4320"
e_ticket_number = printETicketNumber(first_name, string)
print(e_ticket_number)
