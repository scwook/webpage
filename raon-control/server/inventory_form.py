import os
import time

from pvaccess import *
from flask import Flask, jsonify
from flask import request
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = '/home/scwook/flask/upload'

# @app.route('/', methods = ['GET', 'POST'])
# def get_data():
#     print(request.form)
#     file = request.files['file']
#     print(file.filename)

#     filename = secure_filename(file.filename)
#     file.save(os.path.join('/home/scwook', filename))
#     return 'OK'

@app.route('/inventory/insert', methods=['GET', 'POST'])
def set_asset_list():
    conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
    inventory = conn.cursor()
    retrieve = conn.cursor()
    # jsonData = request.get_json()
    formData = request.form

    assetNum = "'" + formData['assetNum'] + "'"
    date = "'" + formData['date'] + "'"
    deviceName = "'" + formData['deviceName'] + "'"
    manager = "'" + formData['manager'] + "'"
    location = "'" + formData['location'] + "'"

    file = request.file['file']
    sercureFileName = secure_filename(file.filename)
    fileName = "'" + sercureFileName + "'"

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
        file.save(os.path.join(folder, sercureFileName))
        return 'success'

    else:
        return 'fail'

    #return json.dumps(jsonData)

if __name__ == "__main__":
    app.run(host="localhost", port="8080")

