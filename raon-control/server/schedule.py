import time
import pymysql
import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SERVER_ADDR = 'localhost'
DB_HOST = 'localhost'
DB_USER = 'scwook'
DB_PASSWORD = 'qwer1234'
DB_DATABASE = 'shift'

@app.route('/schedule/<date>')
def get_data(date):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    schedule = conn.cursor()
    detail = conn.cursor()
    shifter = conn.cursor()
    shiftArray = []

    month = date
    search = month + '-%'
    retrieveQuery = 'SELECT * FROM schedule WHERE fromDate LIKE ' +  "'" + search + "'"

    schedule.execute(retrieveQuery)

    for x in schedule:
        queryString = 'SELECT * FROM detail WHERE schedule LIKE ' + str(x[0])
        detail.execute(queryString)

        queryString = 'SELECT * FROM shifter WHERE schedule LIKE ' + str(x[0])
        shifter.execute(queryString)

        detailArray = []
        shifterArray = []
        for y in detail:
            detailArray.append(y[1])

        for z in shifter:
            shifterDic = {'name':z[1], 'team':z[2], 'desk':z[3], 'seat':z[4], 'leader':z[5] }
            shifterArray.append(shifterDic)


        shiftData = { 'fromDate': x[1], 'toDate':x[2], 'title':x[3], 'detail':detailArray, 'shifter':shifterArray }
        shiftArray.append(shiftData)

    conn.close()

    return json.dumps(shiftArray)

if __name__ == "__main__":
    app.run(host=SERVER_ADDR, port="9011")
