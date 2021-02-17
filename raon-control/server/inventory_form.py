import os
import time
import pymysql

from flask import Flask, jsonify
from flask import request
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = '/home/scwook/flask/upload'

@app.route('/inventory/insert', methods=['POST'])
def set_asset_list():
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    inventory = conn.cursor()
    retrieve = conn.cursor()
    # jsonData = request.get_json()
    formData = request.form

    assetNum = "'" + formData['assetNumber'] + "'"
    date = "'" + formData['assetDate'] + "'"
    deviceName = "'" + formData['assetName'] + "'"
    manager = "'" + formData['assetManager'] + "'"
    location = "'" + formData['assetLocation'] + "'"

    file = request.files['file']
    #sercureFileName = secure_filename(file.filename)
    fileName = "'" + file.filename + "'"
   
    retrieveQuery = 'SELECT * FROM asset_list WHERE AssetNumber LIKE ' + assetNum
    retrieve.execute(retrieveQuery)
    result = retrieve.fetchall()

    if len(result):
        return 'overlap'

    insertQuery = 'INSERT INTO asset_list(AssetNumber,Date,DeviceName,Manager,Location,FileName) VALUES(' + assetNum + "," + date + "," + deviceName + "," + manager + "," + location + "," + fileName + ")"

    inventory.execute(insertQuery)
    conn.commit()

    retrieveQuery = 'SELECT max(ID) FROM asset_list'
    inventory.execute(retrieveQuery)
    lastID = inventory.fetchone()[0]

    conn.close()

    folder = UPLOAD_FOLDER + '/' + str(lastID)
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    if file:
        file.save(os.path.join(folder, file.filename))
        return 'success'

    else:
        return 'fail'

   # return 'OK'
  #return json.dumps(jsonData)

@app.route('/inventory/update', methods=['POST'])
def update_asset_list():
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    
    inventory = conn.cursor()
    updateQuery = 'UPDATE asset_list SET fileName = "test.jpg" WHERE ID = 1'


    inventory.execute(updateQuery)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.run(host="192.168.68.126", port="8080")
