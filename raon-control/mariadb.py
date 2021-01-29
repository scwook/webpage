import pymysql

conn = pymysql.connect(host='localhost', user='scwook', password='light299', db='shift', charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM schedule")
data = cur.fetchone()
print (data)
conn.close()
