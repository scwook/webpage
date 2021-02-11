import time
import pymysql
import json

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/inventory', methods=['GET', 'POST'])
def get_inventory():
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    inventory = conn.cursor()
    jsonData = request.get_json()
    print(jsonData)
    #temp = {'assetNum':'20130619', 'date':'2013-06', 'deviceName':'IPhone', 'manager':'Son, Changwook', 'location':'SCL3 Gallery','fileName':'pict$    assetNum = "'" + jsonData['assetNum'] + "'"
    date = "'" + jsonData['date'] + "'"
    deviceName = "'" + jsonData['deviceName'] + "'"
    manager = "'" + jsonData['manager'] + "'"
    location = "'" + jsonData['location'] + "'"
    fileName = "'" + jsonData['fileName'] + "'"

    insertQuery = 'INSERT INTO asset_list(AssetNumber,Date,DeviceName,Manager,Location,FileName) VALUES(' + assetNum + "," + date + "," + deviceNam$    inventory.execute(insertQuery)
    conn.commit()
    conn.close()

    #return insertQuery
    #data = request.get_json()
    #print(data)
    return json.dumps(jsonData)

if __name__ == "__main__":
    app.run(host="192.168.0.105", port="8080")