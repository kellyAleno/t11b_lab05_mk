from flask import redirect, render_template, request, url_for
from server import app, user_input

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        string = request.form["string"]
        new_list = [int(n) for n in string.split(',')]
        bubbleSort(new_list)

        return redirect(url_for('sort'))
    return render_template('index.html')

@app.route('/sort')
def sort():
    copy = []

    for a in user_input:
        copy.append(a)
    user_input.clear()
    return render_template('sort.html', all_users=copy)

def bubbleSort(alist):
    for a in range(len(alist) - 1, 0, -1):
        for i in range(a):
            change = 0
            if alist[i] > alist[i + 1]:
                change = 1
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
            if change == 1:
                user_input.append(str(alist))
