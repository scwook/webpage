import time
import pymysql
import json

from pvaccess import *
from flask import Flask, jsonify
from flask_cors import CORS

jsonData = dict()
test = {'a':'b'}

class ChannelMonitor:
    def __init__(self, name):
        self.name = name

    def monitor(self, data):
        jsonData[self.name] = data.toJSON(False)
	print(jsonData[self.name])

### Read Channel List
pvList = list(line.strip() for line in open('pvList'))

channelList = list()
monitoringList = list()

index = 0
for name in pvList:
        channelList.append(Channel(name, ProviderType.CA))
        monitoringList.append(ChannelMonitor(name))

        channelList[index].monitor(monitoringList[index].monitor, 'field(value,alarm)')
        index += 1


### Flask App
app = Flask(__name__)
CORS(app)

@app.route('/')
def get_data():
        return json.dumps(jsonData)


if __name__ == "__main__":
    app.run(host="192.168.0.105", port="8080")
