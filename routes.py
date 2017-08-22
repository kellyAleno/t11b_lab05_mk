from flask import redirect, render_template, request, url_for
from server import app
import csv

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # name = request.form["name"]
        # zID = int(request.form["zID"])
        # description = request.form["desc"]
        string = request.form["string"]
        with open('example.csv', 'a') as csv_out:
            writer = csv.writer(csv_out)
            writer.writerow([name, zID, description])

        return redirect(url_for('hello'))
    return render_template('index.html')

@app.route('/Hello')
def hello():
    user_input = []
    with open('example.csv', 'r') as csv_in:
        reader = csv.reader(csv_in)
        for row in reader:
            user_input.append(row)
            # user_input.append([row[0], row[1], row[2]])

    return render_template('Hello.html', all_users=user_input)

