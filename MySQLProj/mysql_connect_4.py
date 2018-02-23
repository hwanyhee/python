#coding:utf-8
import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='choi',
   password='mysql1234', db='my_suppliers', charset='utf8',
     cursorclass=pymysql.cursors.DictCursor)
     # cursorclass=pymysql.cursors.DictCursor는 딕셔너리 형태로 출력되고
     # 이 부분을 생략하면 결과가 튜플 형태로 출력된다.

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
sql = "select * from Suppliers"
curs.execute(sql)

# 데이터 Fetch
rows = curs.fetchall()
#row = curs.fetchone()

#print(row) #전체 내용 출력

for row in rows:
	#print(row)
	print(row)

# Connection 닫기

conn.close()
