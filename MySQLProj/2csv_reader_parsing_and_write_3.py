import sys #csv 모듈을 사용하여 입력 파일을 파싱하고 출력 파일에 쓸 수 있게 한다.
import csv
#suppliers_data.csv 2python_output.csv
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r',encoding='utf-8', newline='') as csv_in_file:
   with open(output_file, 'w',encoding='utf-8',newline='') as csv_out_file:
      # 입력 파일을 읽는 객체 생성
      filereader = csv.reader(csv_in_file, delimiter=',')
      # 출력 파일에 Tm는 객체 생성
      filewriter = csv.writer(csv_out_file, delimiter=',') # delimiter=',' 인수
            # 는 기본값이므로 입력 및 출력 파일이 쉼표로 구분된 경우라면 굳이 쓰지 않아도 되
            # 며, 다른 구분 기호, 예를 들어 세미콜론(;), 탭(\t)으로 구분된 입력 파일을 읽거나
            # 출력 파일을 작성하고 싶다면 구분 기호 인수를 지정해야 한다.
      for row_list in filereader:
          print(row_list)
          filewriter.writerow(row_list) # 각 행의 값을 리스트 자료형으로 출력 파일에
                                                 # 쓴다.