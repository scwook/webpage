import pymysql
import json

conn = pymysql.connect(host='localhost', user='scwook', password='light299', db='shift', charset='utf8')
schedule = conn.cursor()
detail = conn.cursor()
shifter = conn.cursor()
shiftArray = []

month = '2021-01'
search = month + '-%'

retrieveQuery = 'SELECT * FROM schedule WHERE fromDate LIKE ' +  "'" + search + "'"
print(retrieveQuery)
#cur.execute("SELECT * FROM schedule")
schedule.execute(retrieveQuery)
#schedule.execute("SELECT * FROM schedule WHERE fromDate LIKE '2021-01-%'")
#data = json.dumps(cur.fetchall())
for x in schedule:
    queryString = 'SELECT * FROM detail WHERE schedule LIKE ' + str(x[0])
    detail.execute(queryString)

    queryString = 'SELECT * FROM shifter WHERE schedule LIKE ' + str(x[0])
    shifter.execute(queryString)

    detailArray = []
    shifterArray = []
    for y in detail:
        detailArray.append(y[1])

    for z in shifter:
	shifterDic = {'name':z[1], 'team':z[2], 'desk':z[3], 'seat':z[4], 'leader':z[5] }
	shifterArray.append(shifterDic)

    shiftData = { 'fromDate': x[1], 'toDate':x[2], 'title':x[3], 'detail':detailArray, 'shifter':shifterArray }

    shiftArray.append(shiftData)

    #print(detail.fetchall())

conn.close()

print(json.dumps(shiftArray, indent=4))
