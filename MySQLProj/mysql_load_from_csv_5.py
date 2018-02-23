# coding:utf-8

import csv
import MySQLdb  # MySQLdb 모듈을 임포트하여 MySQL 데이터베이스와 테이블에 연결하는데,
# pip3로 설치할 때 사용한 패키지명인 mysqlclient와는 다른 이름으로 사용한다는
# 점에 주의해야 한다.
import sys

from datetime import datetime, date

# CSV 입력 파일 경로와 파일명
#suppliers_data.csv
input_file = sys.argv[1]

# MySQL Connection 연결
conn = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers',
                       user='choi', passwd='mysql1234', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# 파일 읽기
# Suppliers 테이블에 데이터를 입력한다.:구분자를 \t로 해줘야 함
file_reader = csv.reader(open(input_file, 'r',encoding='utf-8'), delimiter='\t')
header = next(file_reader)

for row in file_reader:  # 입력 파일의 모든 행을 반복 처리
    data = []  # 빈 리스트를 생성하여 INSERT문에서 필요한 값들로 채워진다.

    for column_index in range(len(header)):  # 각 행에 있는 모든 열들을 반복 처리
        if column_index < 4:  # 열 인덱스가 4보다 작은지 비교, 즉, 입력 파일은 5개의 열이 있으
            # 며, 이 중 날짜 정보는 5번째 열에 있으므로 날짜 열의 인덱스는 4 이다.

            data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
            # 0,1,2,3의 인덱스 값을 지닌 열에 대해 실행하고 해당 열의 값을 문자열로 변환하고
            # $ 기호가 있으면 제거한다.
        else:

            #데이타 형식에 맞게 %m/%d/%Y 바꾸아야함
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%Y'))
            # 인덱스 값이 4인 마지막 날짜 열을 문자열로 바꾸고 입력 형식에 따라 해당 문자열을
            # datetime 객체로 만든다. # %Y를 사용하면 년도를 2016으로 저장하고 %y를 사용하면
            # 15로 저장한다.
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
        print(data)  # data에 저장된 데이터 행을 출력한다.
    curs.execute("""INSERT INTO Suppliers VALUES(%s, %s, %s, %s, %s);""", data)
# 각각의 %s는print( 입력할 각 변수의 위치를 표시하는 플레이스홀더이며, 개수는 입력 파일에
# 있는 열의 수와 일치해야 하며, 테이블의 열의 수와 일치해야 한다.
# 또한, 순서도 일치해야 한다.

conn.commit()
print("")

# Suppliers 테이블에 질의를 한다.
curs.execute("SELECT * FROM Suppliers")
rows = curs.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)