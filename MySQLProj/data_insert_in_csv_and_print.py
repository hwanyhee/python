import csv
# csv 파일에 2개의 라인을 저장하는 예제
with open('suppliers_data.csv', 'a', encoding='utf-8', newline='') as fd:
 out = csv.writer(fd)
 out.writerow( ['공급자 A','111-234','9999','$400.00' ,'3/21/2017'] )
 out.writerow( ['공급자 A','111-234','9999','$400.00' ,'3/21/2017'] )

 with open('suppliers_data.csv', 'r', encoding='utf-8') as fd:
     cin = csv.reader(fd)
     arrCsv = [row for row in cin]
     print(arrCsv)

# csv 파일을 읽어서 라인별로 출력하는 예제

with open('suppliers_data.csv', 'r', encoding='utf-8') as fd:
    cin = csv.reader(fd)
    for line in cin:
        print( line )
