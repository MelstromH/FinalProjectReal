def printETicketNumber(first_name, string):
    e_ticket_number = "".join([first_name[i] + string[i] for i in range(len(first_name))]) + string[len(first_name):]
    return e_ticket_number