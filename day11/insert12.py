import pymysql
conn=pymysql.connect(
    host='127.0.0.1',port=3306,user='root',passwd='123456',
    db='tedu',charset='utf8'
)

cursor=conn.cursor()
insert1='insert into departments(dep_id,dep_name) VALUES (%s,%s)'
data=[(1,'人事部')(2,'运维部'),(3,'开发部')]
result1=cursor.executemany(insert1,data)
conn.commit()
cursor.close()
conn.close()

