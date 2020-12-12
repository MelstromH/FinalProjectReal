first_name = "John"
seat_row = 2
seat_column = 3
string = "INFOTC4320"

#Credit to https://blog.finxter.com/how-to-interleave-two-strings-of-variable-lengths-python/
e_ticket_number = "".join([first_name[i] + string[i] for i in range(len(first_name))]) + string[len(first_name):]

print(e_ticket_number)


fileToWrite = open("reservation.txt", "w")
fileToWrite.write(first_name + " " + str(seat_row) + " " + str(seat_column) + " " + str(e_ticket_number))
fileToWrite.close()

