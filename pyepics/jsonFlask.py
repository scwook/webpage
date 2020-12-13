import time
from pvaccess import *
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def get_data():
    data = {'name' : 'scwook', 'age' : '38'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="192.168.0.9", port="8080")

