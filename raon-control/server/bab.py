import time
import pymysql
import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_HOST = 'localhost'
DB_USER = 'scwook'
DB_PASSWORD = 'qwer1234'
DB_DATABASE = 'bab'

@app.route('/bab/retrieve')
def get_data(date):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DATABASE, charset='utf8')
    bab = conn.cursor()

    babArray = []

    retrieveQuery = 'SELECT * FROM bab_list'

    bab.execute(retrieveQuery)

    for x in bab:
        babList = { 'menu': x[0], 'location':x[1], 'kind':x[2], 'price':x[3], 'tier':x[4] }
        babArray.append(babList)

    conn.close()

    return json.dumps(babArray)

if __name__ == "__main__":
    app.run(host=SERVER_ADDR, port="8082")
