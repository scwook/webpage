import pymysql
import json
import datetime

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SERVER_ADDR = 'localhost'
DB_HOST = 'localhost'
DB_USER = 'ctrluser'
DB_PASSWORD = 'qwer1234'
DB_DATABASE = 'tachine'

@app.route('/tachine/event', methods=['POST'])
def create_event():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    tachine = conn.cursor()

    jsonData = request.get_json()

    # Insert new event
    dateNow = "'" + str(datetime.datetime.now()) + "'"
    eventTitle = "'" + jsonData['title'] + "'"

    insertEventQuery = 'INSERT INTO event(date,title) values(' + dateNow + "," + eventTitle + ")"
    tachine.execute(insertEventQuery)
    conn.commit()

    lastEventQuery = 'SELECT max(eventid) FROM event'
    tachine.execute(lastEventQuery)
    lastEventID = str(tachine.fetchone()[0])
    lastEventIDStr = "'" + str(tachine.fetchone()[0]) + "'"

    # Insert new snapshot
    snapshotDescription = "'" + jsonData['description'] + "'"

    insertSnapshotQuery = 'INSERT INTO snapshot_info(description,eventid) values(' + snapshotDescription + "," + lastEventIDStr + ")"
    tachine.execute(insertSnapshotQuery)
    conn.commit()

    lastSnapshotQuery = 'SELECT max(snapshotid) FROM snapshot_info'

    tachine.execute(lastSnapshotQuery)
    lastSnapshotID = str(tachine.fetchone()[0])
    
    # Create snapshot table
    createTableQuery = 'CREATE TABLE snapshot_' + lastSnapshotID + '(pvname varchar(255) NOT NULL, value varchar(255))'
    tachine.execute(createTableQuery)
    conn.commit()

    conn.close()

    tachineDic = {'eventid' : lastEventID, 'snapshotid' : lastSnapshotID}

    return json.dumps(tachineDic)

@app.route('/tachine/snapshot/<snapshotData>', methods=['POST'])
def create_snapshot(snapshotData):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    tachine = conn.cursor()

    eventID = snapshotData['eventid']
    snapshotDescription = snapshotData['description']

    insertQuery = 'INSERT INTO snapshot_info(description,eventid) values(' + snapshotDescription + "," + eventID + ")"
    tachine.execute(insertQuery)
    conn.commit()

    lastSnapshotQuery = 'SELECT max(snapshotid) FROM snapshot_info'
    tachine.execute(lastSnapshotQuery)
    lastSnapshotID = tachine.fetchone()[0]

    createTableQuery = 'CREATE TABLE snapshot_' + lastSnapshotID + '(pvname varchar(255) NOT NULL, value varchar(255))'
    tachine.execute(createTableQuery)

    tachineDic = {'snapshotid' : lastSnapshotID}

    return json.dumps(tachineDic)


if __name__ == "__main__":
    app.run(host=SERVER_ADDR, port="9013")
