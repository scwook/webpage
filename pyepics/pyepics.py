import time
from pvaccess import *

class ChannelMonitor:
    def __init__(self, name):
        self.name = name

    def monitor(self, data):
        jsonData = data.toJSON(False)
#        self.writeDataToFile(self.name, jsonData)
        print(jsonData)

    def writeDataToFile(self, fileName, data):
        newFileName = fileName.replace(":", "-")
        f = open(newFileName, 'w')
        f.write(data)
        f.close()

### Read Channel List
pvList = list(line.strip() for line in open('pvList'))

channelList = list()
monitoringList = list()

index = 0
for name in pvList:
	channelList.append(Channel(name, ProviderType.CA))
	monitoringList.append(ChannelMonitor(name))

	channelList[index].monitor(monitoringList[index].monitor)
	index += 1

while 1:
    time.sleep(1)
