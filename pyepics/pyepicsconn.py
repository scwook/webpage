import time
import json

from pvaccess import *

c = MultiChannel(['scwookHost:ai1','scwookHost:ai2','scwookHost:ai3'], ProviderType.CA)
channel = Channel('out', ProviderType.CA)

count = 0
pvObjectDict = dict()

class ChannelMonitor:
    def __init__(self, name):
        self.name = name

    def isConnected(self, status):
        pvObjectDict[self.name] = status
        print(json.dumps(pvObjectDict))


channel.setConnectionCallback(ChannelMonitor('out').isConnected)


test = [{'pvname':'scwook'},{'pvname':'scwook2'}]

for name in test:
    print(name['pvname'])

while 1:
        count += 1
        print(count)
	time.sleep(1)
