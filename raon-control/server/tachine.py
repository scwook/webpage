import pymysql
import json

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

    # create snashot table
    snapshotNumber = str(pvList)
    print(pvList)
    tableCreateQuery = 'CREATE TABLE snapshot_' + snapshotNumber + '(pvname varchar(255) NOT NULL, value varchar(255))'
    tachine.execute(tableCreateQuery)
    conn.commit()



    conn.close()

    return 'ok'


@app.route('/tachine/getid')
def get_last_id():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    tachine = conn.cursor()

    getLastEventQuery = 'SELECT max(eventid) FROM event'
    getLastSnapshot = 'SELECT max(snapshotid) FROM snapshot_info'
    return 'ok'

@app.route('/inventory/retrieve/<asset>')
def get_asset_list(asset):

    return 'ok'

if __name__ == "__main__":
    app.run(host=SERVER_ADDR, port="9010")
