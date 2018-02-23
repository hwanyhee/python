import sys
import pandas as pd
#suppliers_data.csv pandas_output.csv
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)