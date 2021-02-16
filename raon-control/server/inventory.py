import os
import time
import pymysql
import json

from flask import Flask, jsonify
from flask import request
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = '/home/scwook/flask/upload'

@app.route('/inventory/insert', methods=['GET', 'POST'])
def set_asset_list():
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    inventory = conn.cursor()
    retrieve = conn.cursor()
    jsonData = request.get_json()

    assetNum = "'" + jsonData['assetNum'] + "'"
    date = "'" + jsonData['date'] + "'"
    deviceName = "'" + jsonData['deviceName'] + "'"
    manager = "'" + jsonData['manager'] + "'"
    location = "'" + jsonData['location'] + "'"
    fileName = "'" + jsonData['fileName'] + "'"

    retrieveQuery = 'SELECT * FROM asset_list WHERE AssetNumber LIKE ' + assetNum
    retrieve.execute(retrieveQuery)
    result = retrieve.fetchall()

    if len(result):
        return 'overlap'

    insertQuery = 'INSERT INTO asset_list(AssetNumber,Date,DeviceName,Manager,Location,FileName) VALUES(' + assetNum + "," + date + "," + deviceName + "," + manager + "," + location + "," + fileName + ")"

    inventory.execute(insertQuery)
    conn.commit()
    conn.close()

    #return json.dumps(jsonData)
    return 'success'

@app.route('/inventory/insert', methods=['GET', 'POST'])
def update_asset_list():
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    inventory = conn.cursor()
    updateQuery = 'UPDATE asset_list SET fileName = "test.jpg" WHERE ID = 1'

    inventory.execute(updateQuery)
    conn.commit()
    conn.close()

@app.route('/inventory/retrieve/<asset>')
def get_asset_list(asset):
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    inventory = conn.cursor()
    inventoryArray = []

    search = asset.replace("*", "%")
    retrieveQuery = 'SELECT * FROM asset_list WHERE AssetNumber LIKE ' + "'" + search + "'"

    inventory.execute(retrieveQuery)

    for x in inventory:
        inventoryDic = {'id':x[0], 'assetNum':x[1], 'date':x[2], 'deviceName':x[3], 'manager':x[4], 'location':x[5], 'fileName':x[6]}
        inventoryArray.append(inventoryDic)
    
    conn.close()

    return json.dumps(inventoryArray, ensure_ascii=False)

@app.route('/inventory/upload', methods=['GET', 'POST'])
def file_save():
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    inventory = conn.cursor()
    
    retrieveQuery = 'SELECT max(ID) FROM asset_list'
    inventory.execute(retrieveQuery)
    lastID = inventory.fetchone()[0]

    folder = UPLOAD_FOLDER + '/' + str(lastID)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if request.method == 'POST':
        # check if the post request has the file part
        #if 'file' not in request.files:
        #    flash('No file part')
        #    return redirect(request.url)

        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        #if file.filename == '':
        #    flash('No selected file')
        #    return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            return 'success'
        else:
            return 'fail'


if __name__ == "__main__":
    app.run(host="localhost", port="8080")