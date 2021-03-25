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

SERVER_ADDR = 'localhost'
DB_HOST = 'localhost'
DB_USER = 'ctrluser'
DB_PASSWORD = 'qwer1234'
DB_DATABASE = 'tachine'

@app.route('/tachine/insert/<pvList>', methods=['POST'])
def set_snapshot():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    tachine = conn.cursor()

@app.route('/inventory/retrieve/<asset>')
def get_asset_list(asset):

if __name__ == "__main__":
    app.run(host=SERVER_ADDR, port="9010")
