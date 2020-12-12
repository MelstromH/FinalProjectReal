from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *
from .functions import *


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if checkCreds(username, password) == 1:
            loginOK = 1
            mapVar = populateChart()
            totalCost = getTotalRevenue()
            return render_template("admin.html", mapVar=mapVar, loginOK=loginOK, totalCost=totalCost, form=form, template="form-template")

        else:
            error="Invalid credientials, please try again"
            return render_template("admin.html", form=form,error = error, template="form-template")
        
        

    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()
    mapVar = populateChart()
    if request.method == 'POST' :
        chart = ""
        info = ""
        error = ""
        mapVar = populateChart()
        if form.validate_on_submit():
            firstName = request.form['first_name']
            string = "INFOTC4320"
            row = request.form['row']
            seat = request.form['seat']
            rowSeat = rowandSeat(row, seat)
            e_ticket_number = printETicketNumber(firstName, string)
            chart = e_ticket_number
            info = rowSeat
            # mapRow = str(row)
            # mapSeat = str(seat)
            # flightMap = printFlightMap( "flight", mapRow, mapSeat)
            arrayRow = int(row) - 1
            arraySeat = int(seat) -1
            if checkSeat(arrayRow,arraySeat) == 0:
                filetoWrite = open("reservation.txt", "a")
                filetoWrite.write(firstName + ", " + str(arrayRow) + ", " + str(arraySeat) + ", " + str(e_ticket_number + "\n"))
                filetoWrite.close()
            else:
                error = "Error: Seat already taken. Please select another"
            mapVar = populateChart()
        return render_template("reservations.html", error = error, form=form, template="form-template", chart= chart, info = info, mapVar = mapVar)

    return render_template("reservations.html", form=form, mapVar=mapVar, template="form-template")

