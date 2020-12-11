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

    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()
    if request.method == 'POST' :
        chart = ""
        info = ""
        if form.validate_on_submit():
            firstName = request.form['first_name']
            string = "INFOTC4320"
            row = request.form['row']
            seat = request.form['seat']
            rowSeat = rowandSeat(row, seat)
            e_ticket_number = printETicketNumber(firstName, string)
            chart = e_ticket_number
            info = rowSeat
            filetoWrite = open("reservation.txt", "w")
            filetoWrite.write(firstName + " " + str(row) + " " + str(seat) + " " + str(e_ticket_number))
            filetoWrite.close()
        return render_template("reservations.html", form=form, template="form-template", chart= chart, info = info)

    return render_template("reservations.html", form=form, template="form-template")

