import flask
from flask import render_template, url_for, redirect, request, jsonify, Response
from firebase import firebase

app = flask.Flask(__name__)

db_url = 'https://hcip-7c360-default-rtdb.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)

@app.route('/', methods=['GET', 'POST'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('parking', username=request.form.get('username')))
    return render_template('login.html')


@app.route('/parking', methods=['GET', 'POST'])
def parking():
    users = fdb.get('/block', None)  #None全部讀取，1代表讀取第一筆，以此類推
    colors = dict()
    for user in users:
        if users[user] == "None":
            colors[user] = "#AAFF00" 
        else:
            colors[user] = "red"
        print(user, users[user], colors[user])
    return render_template('parking.html', datas=users, color=colors)


if __name__ == '__main__':
    app.debug = True
    app.run()

    
    
