import csv
import MySQLdb
import sys
#data_for_updating_mysql.csv
input_file = sys.argv[1]

conn = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers',
                  user='choi', passwd='mysql1234', charset='utf8')

curs = conn.cursor()

# CSV 파일을 읽고 특정 행을 갱신한다.
file_reader = csv.reader(open(input_file, 'r',encoding='utf-8', newline=''), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    curs.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)
    conn.commit()

# Suppliers 테이블에 질의를 한다.
curs.execute("SELECT * FROM Suppliers")
rows = curs.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)

conn.close()