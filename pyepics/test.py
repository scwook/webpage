import time
from pvaccess import *

def echo(x):
    print(x.toJSON(False))

c = Channel('scwookHost:ai1', ProviderType.CA)
#c.monitor(echo)
c.subscribe('echo', echo)
c.startMonitor()

while 1:
    time.sleep(1)
