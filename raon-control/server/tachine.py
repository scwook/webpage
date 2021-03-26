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

@app.route('/tachine/snapshot/<pvList>', methods=['POST'])
def set_snapshot(pvList):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    tachine = conn.cursor()

    # create snapshot table
    snapshotNumber = str(pvList)
    print(pvList)
    tableCreateQuery = 'CREATE TABLE snapshot_' + snapshotNumber + '(pvname varchar(255) NOT NULL, value varchar(255))'
    tachine.execute(tableCreateQuery)
    conn.commit()

    conn.close()

    return 'ok'

@app.route('/tachine/event/<eventData>', methods=['POST'])
def create_event(eventData):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    tachine = conn.cursor()

    dateNow = datetime.datetime.now()
    eventTitle = eventData['title']

    insertQuery = 'INSERT INTO event(date,title) values(' + dateNow + "," + eventTitle + ")"
    tachine.execute(insertQuery)
    tachineDic.commit()

    lastEventQuery = 'SELECT max(eventid) FROM event'
    tachine.execute(lastEventQuery)
    lastEventID = tachine.fetchone()[0]

    tachineDic = {'eventid' : lastEventID}

    conn.close()

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

@app.route('/inventory/retrieve/<asset>')
def get_asset_list(asset):

    return 'ok'

if __name__ == "__main__":
    app.run(host=SERVER_ADDR, port="9010")
