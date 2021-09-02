import json
import pymysql

from flask import Flask, request, render_template, redirect, url_for, abort, session
from flask_bcrypt import Bcrypt
from datetime import timedelta

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config["SECRET_KEY"] = b'koownos!#gnoeymik/'
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)

SERVER_ADDR = 'localhost'
DB_HOST = 'localhost'
DB_USER = 'ctrluser'
DB_PASSWORD = 'qwer1234'
DB_DATABASE = 'users'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    jsonData = request.get_json()

    if 'id' not in jsonData or 'pw' not in jsonData:
        return 'Check User ID or Password', 300

    id = jsonData['id']
    pw = jsonData['pw']

    if len(id) == 0 or len(pw) == 0:
        return 'Check User ID or Password', 300

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    dbCursor = conn.cursor()

    retrieveQuery = 'SELECT * FROM user_info WHERE ID = %s;'
    dbCursor.execute(retrieveQuery, id)

    recordCount = dbCursor.rowcount
    if recordCount == 0:
        return 'Check User ID or Password', 300

    userInfo = dbCursor.fetchone()
    checkPassword = bcrypt.check_password_hash(userInfo[2], pw)

    conn.close()

    if checkPassword:
        session['user'] = id
        session.permanet = True
        return session['user'], 200

    return 'Check User ID or Password', 300

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')

    jsonData = request.get_json()

    if 'id' not in jsonData or 'pw' not in jsonData:
        return 'Check User ID or Password', 300

    id = jsonData['id']
    pw = jsonData['pw']
    username = jsonData['username']

    if len(id) == 0 or len(pw) == 0:
        return 'Check User ID or Password', 300

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    dbCursor = conn.cursor()

    print(id, pw, username)
    retrieveQuery = 'SELECT * FROM user_info WHERE ID = %s;'
    dbCursor.execute(retrieveQuery, id)

    recordCount = dbCursor.rowcount
    if userCount != 0:
        return 'ID Already Exist', 300

    hashed_password = bcrypt.generate_password_hash(pw)
    userInfo = (id, hashed_password, username)

    insertQuery = 'INSERT INTO user_info (ID, Password, Username) VALUES(%s, %s, %s);'
    dbCursor.execute(insertQuery, userInfo)
    
    conn.commit()
    conn.close()

    return 'Done', 200

@app.route('/update', methods=['GET', 'POST'])
def update():
    if 'user' not in session:
        return render_template('login.html')

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    dbCursor = conn.cursor()

    print(request.method)
    if request.method == 'GET':

        id = session['user']

        retrieveQuery = 'SELECT * FROM user_info WHERE ID = %s;'
        dbCursor.execute(retrieveQuery, id)
    
        userInfo = dbCursor.fetchone()
        # print(userInfo[0], userInfo[1], userInfo[2], userInfo[3])

        returnData = {'id' : userInfo[1], 'username' : userInfo[3]}      

        return render_template('update.html', data = returnData)

    if request.method == 'POST':

        jsonData = request.get_json()

        if 'id' not in jsonData or 'pw' not in jsonData:
            return 'Check User ID or Password', 300

        id = jsonData['id']
        pw = jsonData['pw']
        username = jsonData['username']

        if len(id) == 0 or len(pw) == 0:
            return 'Check User ID or Password', 300

        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
        dbCursor = conn.cursor()

        print(id, pw)
        hashed_password = bcrypt.generate_password_hash(pw)
        userInfo = (hashed_password, username, id)

        updateQuery = 'UPDATE user_info SET Password = %s, Username = %s WHERE ID = %s;'
        dbCursor.execute(updateQuery, userInfo)

        conn.commit()
        conn.close()

        return 'OK', 200

    return 'Error', 300

@app.route('/main')
def main():
    print(session)
    if 'user' in session:
        return render_template('main.html')

    return redirect(url_for('login'))

@app.route('/monitoring')
def monitoring():
    if 'user' in session:
        print(session)
        return render_template('monitoring.html')

    return redirect(url_for('login'))

@app.route('/schedule')
def monitoring():
    if 'user' in session:
        print(session)
        return render_template('schedule.html')

    return redirect(url_for('login'))

@app.route('/archive')
def archive():
    if 'user' in session:
        print(session)
        return render_template('archive.html')

    return redirect(url_for('login'))

@app.route('/download')
def monitoring():
    if 'user' in session:
        print(session)
        return render_template('download.html')

    return redirect(url_for('login'))

@app.route('/document')
def monitoring():
    if 'user' in session:
        print(session)
        return render_template('docuemnt.html')

    return redirect(url_for('login'))


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET return'
    else:
        num = request.form["num"]
        name = request.form["name"]
        return 'POST, num: {} name: {}'.format(num, name)

if __name__ == "__main__":
    app.run(host="192.168.68.126", port="8080", debug=True)
