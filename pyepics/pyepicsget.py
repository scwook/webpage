import time
from pvaccess import *

c = MultiChannel(['scwookHost:ai1','scwookHost:ai2','scwookHost:ai3'], ProviderType.CA)

while 1:
	print c.get().toJSON(False)
	time.sleep(1)
