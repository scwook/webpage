import time

from pvaccess import *

provider = ProviderType.CA

### Read Channel List
pvListSet = set(line.strip() for line in open('pvList'))

ch = {}

for pvName in pvListSet:
    ch[pvName] = Channel(pvName, provider)

while True:
    for key, value in ch.items():
        parsingJSON = value.get('').toJSON(False)
        f = open(key, "w")
        f.write(parsingJSON)
        f.close()

    time.sleep(1)

print('End')

