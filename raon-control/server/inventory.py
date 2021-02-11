import time
import pymysql
import json

from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/inventory', methods=['GET', 'POST'])
def get_inventory():
    #conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    #inventory = conn.cursor()
    #temp = {'assetNum':'20130619', 'date':'2013-06', 'deviceName':'IPhone', 'manager':'Son, Changwook', 'fileName':'picture.jpg'}
    #insertQuery = 'INSERT INTO asset_list VALUES(NULL,' + temp['assetNum'] + "," + temp['date'] + "," + temp['deviceName'] + "," + temp['manager'] + "," + temp['fileName'] + ")"
    #return insertQuery
    # data = request.get_json()

    return 'aaa'

if __name__ == "__main__":
    app.run(host="192.168.0.105", port="8080")
