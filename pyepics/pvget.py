import time
from pvaccess import *
from flask import Flask, jsonify

c = MultiChannel(['scwookHost:ai1','scwookHost:ai2','scwookHost:ai3'], ProviderType.CA)

app = Flask(__name__)
@app.route('/')
def get_data():
    return c.get().toJSON(False)

if __name__ == "__main__":
    app.run(host="192.168.68.126", port="8080")
