import sys

#suppliers_data.csv python_output.csv
#csv파일을 메모장으로 열어서 반드시 UTF-8로 저장해야 한다
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='UTF8',newline='') as filereader:
    with open(output_file, 'w', encoding='UTF8', newline='') as filewriter:

        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)

        filewriter.write(','.join(map(str,header_list))+'\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')

