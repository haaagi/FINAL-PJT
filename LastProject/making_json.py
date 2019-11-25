# import csv
# import pandas as pd


# a = pd.read_csv('result.csv')
# b = pd.read_csv('plusUrl.csv')
# result = a.merge(b, on='movieCd')
# result.to_csv("result_Url.csv", index=False)

# a = pd.read_csv('result_Url.csv')
# b = pd.read_csv('movie_des.csv')
# result = a.merge(b, on='movieCd')
# result.to_csv("final.csv", index=False)


import csv
import json
input_file_name = "final.csv"
output_file_name = "data2.json"
with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
        open(output_file_name, "w", encoding="utf-8", newline="") as output_file:
        
    reader = csv.reader(input_file)
    # 첫 줄은 col_names 리스트로 읽어 놓고
    col_names = next(reader)
    # 그 다음 줄부터 zip으로 묶어서 json으로 dumps
    for cols in reader:
        doc = {col_name: col for col_name, col in zip(col_names, cols)}
        print(json.dumps(doc, ensure_ascii=False), file=output_file)