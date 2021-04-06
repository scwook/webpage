import time
import json
import threading

from pvaccess import *

c = MultiChannel(['scwookHost:ai1','scwookHost:ai2','scwookHost:ai3'], ProviderType.CA)
channel = Channel('out', ProviderType.CA)

count = 0
snapshotRecordDict = dict()
#pvObjectDict = dict()
channelList = list()
#monitoringList = list()
#monitoringDict = dict()

class ChannelMonitor:
    def __init__(self, snapshotid, name):
        self.snapshotid = snapshotid
        self.name = name

    def isConnected(self, status):
        snapshotRecordDict[self.snapshotid][self.name] = status
        print('conn')

#channel.setConnectionCallback(ChannelMonitor('out').isConnected)


#test = [{'pvname':'SYS-SUBSYS:DEV-SNAP01:out1'},{'pvname':'SYS-SUBSYS:DEV-SNAP01:out2'},{'pvname':'SYS-SUBSYS:DEV-SNAP01:out7'}]
test = [{'pvname':'out'},{'pvname':'input'},{'pvname':'scwook'}]


snapshotid = 6
recordStatusDict = dict()

index = 0
for name in test:
    pvname = name['pvname']
    print(pvname)

    recordStatusDict['pvname'] = 'False'
    snapshotRecordDict[snapshotid] = recordStatusDict

    channelList.append(Channel(pvname, ProviderType.CA))
    #monitoringDict = {snapshotid : ChannelMonitor(snapshotid, pvname)}

    #print(monitoringDict)
    #monitoringList.append(monitoringDict)

    #print(monitoringList[index])

    #channelList[index].setConnectionCallback(monitoringList[index][snapshotid].isConnected)
    channelList[index].setConnectionCallback(ChannelMonitor(snapshotid, pvname).isConnected)
    
    index += 1

connectionMonitorDict = {snapshotid : channelList}
print(snapsho)

print(connectionMonitorDict)

timerCount = 0
def startTimer(snapshotKey, count):
    timer = threading.Timer(1, startTimer, args=[snapshotKey,count])
    timer.start()
    print('timer count', snapshotKey, count)

    if count > 5:
        #del channelList[-1]
        channel = connectionMonitorDict[snapshotid]
        for i in range(len(channel)):
            #del connectionMonitorDict[snapshotid][-1]
            del channel[-1]

        del snapshotRecordDict[snapshotid]

        timer.cancel()

startTimer([snapshotid,0])

while 1:
        count += 1
        print(snapshotRecordDict)
	time.sleep(1)
