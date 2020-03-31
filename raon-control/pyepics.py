import time

from pvaccess import *

provider = ProviderType.CA

def writeChannelToFile(x):
	f = open(x, 'w')
	f.write(x)
	f.close()

def channelMonitor(field):
	print(field)
#	print(x.toJSON(False))
#	writeChannelToFile(x.toJSON(False))

### Read Channel List
pvListSet = set(line.strip() for line in open('pvList'))

ch = {}

for x in pvListSet:
	ch[x] = Channel(x, provider)
	ch[x].subscribe(x, channelMonitor)
	ch[x].startMonitor()

#print(ch)
### Single Channel
#c = Channel('scwook:ai1', provider)
#c.subscribe('scwook:ai1', channelMonitor)
#c.startMonitor()

#d = Channel('scwook:ai2', provider)
#d.subscribe('scwook:ai2', channelMonitor)
#d.startMonitor('value')

time.sleep(1000)


#print c.get()
#print c.get().toJSON(False)

### Multi Channel
#pvlist = MultiChannel(['scwookHost:ai1','scwookHost:ai2'], provider)
#pvDic = pvlist.get()

#pvDic['value'][0][0]['value']
#pvDic['value'][1][0]['value']
