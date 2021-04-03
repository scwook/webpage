import pymysql
import json
import datetime

from pvaccess import *

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SERVER_ADDR = 'localhost'
DB_HOST = 'localhost'
DB_USER = 'ctrluser'
DB_PASSWORD = 'qwer1234'
DB_DATABASE = 'timeleap'

pvObjectDict = dict()
channelList = list()
monitoringList = list()

class ChannelMonitor:
    def __init__(self, name):
        self.name = name

    def isConnected(self, status):
        pvObjectDict[self.name] = status

@app.route('/timeleap/snapshot/record/connection', methods=['POST'])
def channel_connection_status():

    jsonData = request.get_json()

    index = 0
    for name in jsonData:
        pvname = str(name['pvname'])
        
        channelList.append(Channel(pvname, ProviderType.CA))
        monitoringList.append(ChannelMonitor(pvname))

        channelList[index].setConnectionCallback(monitoringList[index].isConnected)
        index += 1

    return json.dumps(pvObjectDict)



@app.route('/timeleap/event', methods=['POST'])
def create_event():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    timeleap = conn.cursor()

    jsonData = request.get_json()

    # Insert new event
    dateNow = "'" + str(datetime.date.today()) + "'"
    eventTitle = "'" + jsonData['title'] + "'"

    insertEventQuery = 'INSERT INTO event(date,title) values(' + dateNow + "," + eventTitle + ")"
    timeleap.execute(insertEventQuery)
    conn.commit()

    lastEventQuery = 'SELECT max(eventid) FROM event'
    timeleap.execute(lastEventQuery)
    lastEventID = str(timeleap.fetchone()[0])
    lastEventIDStr = "'" + str(lastEventID) + "'"

    # Insert new snapshot
    snapshotTimestamp = "'" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "'"
    snapshotDescription = "'" + jsonData['description'] + "'"

    insertSnapshotQuery = 'INSERT INTO snapshot_info(timestamp,description,eventid) values(' + snapshotTimestamp + "," + snapshotDescription + "," + lastEventIDStr + ")"
    timeleap.execute(insertSnapshotQuery)
    conn.commit()

    lastSnapshotQuery = 'SELECT max(snapshotid) FROM snapshot_info'

    timeleap.execute(lastSnapshotQuery)
    lastSnapshotID = str(timeleap.fetchone()[0])
    
    # Create new snapshot table
    createTableQuery = 'CREATE TABLE snapshot_' + lastSnapshotID + '(pvname varchar(255) NOT NULL, value varchar(255))'
    timeleap.execute(createTableQuery)
    conn.commit()

    conn.close()

    timeleapDic = {'eventid' : lastEventID, 'snapshotid' : lastSnapshotID}

    return json.dumps(timeleapDic)


@app.route('/timeleap/snapshot', methods=['POST'])
def create_snapshot():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    timeleap = conn.cursor()

    jsonData = request.get_json()

    # Insert new snapshot
    eventID = "'" + jsonData['eventid'] + "'"
    snapshotTimestamp = "'" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "'"
    snapshotDescription = "'" + jsonData['description'] + "'"
    
    insertSnapshotQuery = 'INSERT INTO snapshot_info(timestamp,description,eventid) values(' + snapshotTimestamp + "," + snapshotDescription + "," + eventID + ")"
    timeleap.execute(insertSnapshotQuery)
    conn.commit()
    
    lastSnapshotQuery = 'SELECT max(snapshotid) FROM snapshot_info'

    timeleap.execute(lastSnapshotQuery)
    lastSnapshotID = str(timeleap.fetchone()[0])
    
    # Create new snapshot table
    createTableQuery = 'CREATE TABLE snapshot_' + lastSnapshotID + '(pvname varchar(255) NOT NULL, value varchar(255))'
    timeleap.execute(createTableQuery)
    conn.commit()

    conn.close()

    timeleapDic = {'snapshotid': lastSnapshotID}

    return json.dumps(timeleapDic)

@app.route('/timeleap/retrieve', methods=['GET'])
def get_event_snapshot_list():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    eventCursor = conn.cursor()
    snapshotCursor = conn.cursor()

    eventRetrieveQuery = 'SELECT * FROM event'
    eventCursor.execute(eventRetrieveQuery)

    retrieveArray = []
    for x in eventCursor:
        retrieveDic = {'eventid':x[0], 'date':x[1], 'title':x[2], 'snapshot':[]}

        snapshotRetrieveQuery = 'SELECT * FROM snapshot_info WHERE eventid=' + str(x[0])
        snapshotCursor.execute(snapshotRetrieveQuery)
    
        snapshotArray = []
        for y in snapshotCursor:
            snapshotDic = {'snapshotid':y[0], 'timestamp':y[1], 'description':y[2], 'eventid':y[3]}
            snapshotArray.append(snapshotDic)

        retrieveDic['snapshot'] = snapshotArray
        retrieveArray.append(retrieveDic)

    return json.dumps(retrieveArray, ensure_ascii=False)

@app.route('/timeleap/retrieve/event', methods=['GET'])
def get_event_list():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    timeleap = conn.cursor()

    retrieveQuery = 'SELECT * FROM event'
    timeleap.execute(retrieveQuery)

    eventArray = []
    for x in timeleap:
        eventDic = {'eventid':x[0], 'date':x[1], 'title':x[2]}
        eventArray.append(eventDic)

    return json.dumps(eventArray, ensure_ascii=False)

@app.route('/timeleap/retrieve/snapshot', methods=['GET'])
def get_snapshot_list():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    timeleap = conn.cursor()

    retrieveQuery = 'SELECT * FROM snapshot_info'
    timeleap.execute(retrieveQuery)

    snapshotArray = []
    for x in timeleap:
        snapshotDic = {'snapshotid':x[0], 'description':x[1], 'eventid':x[2]}
        snapshotArray.append(snapshotDic)

    return json.dumps(snapshotArray, ensure_ascii=False)

@app.route('/timeleap/retrieve/snapshot/record/<id>', methods=['GET'])
def get_record_list(id):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    timeleap = conn.cursor()

    snapshotID = str(id)

    retrieveQuery = 'SELECT * FROM snapshot_' + snapshotID
    timeleap.execute(retrieveQuery)

    recordArray = []
    for x in timeleap:
        recordDic = {'pvname':x[0], 'value':x[1]}
        recordArray.append(recordDic)

    conn.close()

    return json.dumps(recordArray, ensure_ascii=False)

if __name__ == "__main__":
    app.run(host=SERVER_ADDR, port="9013")
