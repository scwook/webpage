import time
import json

from pvaccess import *

c = MultiChannel(['scwookHost:ai1','scwookHost:ai2','scwookHost:ai3'], ProviderType.CA)
count = 0
while 1:
	print count
        count += 1
	time.sleep(1)
