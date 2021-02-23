import time
import pymysql
import json

from pvaccess import *
from flask import Flask, jsonify
from flask_cors import CORS

mChannel = MultiChannel(['scwookHost:ai1','scwookHost:ai2','scwookHost:ai3'], ProviderType.CA)
data = {'a':'b'}

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_data():
    val = mChannel.get('field(value,alarm)')
#    print(dict(val))
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host="192.168.68.126", port="8080")
