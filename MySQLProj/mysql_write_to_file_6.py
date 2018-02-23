import csv
import MySQLdb
import sys

#mysql_output.csv
output_file = sys.argv[1]

conn = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers',
                  user='choi', passwd='mysql1234', charset='utf8')

curs = conn.cursor()

# 파일 읽기
# Suppliers 테이블에 데이터를 입력한다.
filewriter = csv.writer(open(output_file, 'w',encoding='utf8', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

# Suppliers 테이블을 검색하고 결과를 CSV 파일에 쓴다.
curs.execute("""SELECT * FROM Suppliers
                 WHERE Cost > 700.0;""")#Cost 열이 700보다 큰 레코드 출력
rows = curs.fetchall()
for row in rows:
    filewriter.writerow(row)