import time

from pvaccess import *

class ChannelMonitor:
    def __init__(self, name):
        self.name = name

    def monitor(self, data):
	jsonData = data.toJSON(False)
	self.writeDataToFile(self.name, jsonData)
#        dataDic[self.name] = str(data['value'])

    def writeDataToFile(self, fileName, data):
        f = open(fileName, 'w')
        f.write(data)
        f.close()

#def channelMonitor(field):
#	print(field)
#	print(x.toJSON(False))
#	writeChannelToFile(x.toJSON(False))

### Read Channel List
pvList = list(line.strip() for line in open('pvList'))

pvListLen = len(pvList)

channelList = list()
monitoringList = list()
#dataDic = dict()

index = 0
for name in pvList:
	print(index)
	channelList.append(Channel(name, ProviderType.CA))
	monitoringList.append(ChannelMonitor(name))

	channelList[index].monitor(monitoringList[index].monitor)
	index += 1

#print(ch)
### Single Channel
#c = Channel('scwook:ai1', provider)
#c.subscribe('scwook:ai1', channelMonitor)
#c.startMonitor()

#d = Channel('scwook:ai2', provider)
#d.subscribe('scwook:ai2', channelMonitor)
#d.startMonitor('value')

while 1:
    time.sleep(0.1)


#print c.get()
#print c.get().toJSON(False)

### Multi Channel
#pvlist = MultiChannel(['scwookHost:ai1','scwookHost:ai2'], provider)
#pvDic = pvlist.get()

#pvDic['value'][0][0]['value']
#pvDic['value'][1][0]['value']
