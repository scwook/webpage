import time
from pvaccess import *

class ChannelMonitor:
    def __init__(self, snapshotid):
        self.snapshotid = snapshotid

    def connectionChannel(self, pvname):
        self.pvname = pvname
        self.ch = Channel(pvname, ProviderType.CA)
        self.ch.setConnectionCallback(self.isConnected)

    def isConnected(self, status):
        print(self.snapshotid, self.pvname, status)

d = None
count = 0
while 1:
    print(count)

    if count == 1:
        d = ChannelMonitor(1)
        d.connectionChannel('out')

    if count == 5:
        del f
    
    if count == 15:
        d = ChannelMonitor(1)
        d.connectionChannel('out')
    
    count += 1
    time.sleep(1)