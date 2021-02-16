
import os
import pymysql
import json

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/scwook/flask/upload'

conn = pymysql.connect(host='localhost', user='scwook', password='qwer1234', db='inventory', charset='utf8')
inventory = conn.cursor()
    
retrieveQuery = 'SELECT max(ID) FROM asset_list'
inventory.execute(retrieveQuery)
lastID = inventory.fetchone()[0]
folder = UPLOAD_FOLDER + '/' + str(lastID)
print(folder)
os.makedirs(folder)

