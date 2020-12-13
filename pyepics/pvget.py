import time
from pvaccess import *
from flask import Flask, jsonify

c = Channel('scwook:ai1', ProviderType.CA)

app = Flask(__name__)
@app.route('/')
def get_data():
    return c.get().toJSON(False)

if __name__ == "__main__":
    app.run(host="192.168.0.9", port="8080")
