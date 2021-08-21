import csv
import matplotlib.pyplot as plt

f = open('202107_age.csv')
data = csv.reader(f)

header = next(data)

result = []
for one in data:
    if '안양시' in one[0]:
        # 안양시 인구 데이터 저장
        for cnt in one[3:]:
            cnt = cnt.replace(',','')
            result.append(int(cnt))
        break


print(len(result))