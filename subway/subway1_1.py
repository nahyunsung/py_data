import csv

f = open("2021년_8월_bus.csv")
data = csv.reader(f)

header = next(data)
print(header)

max = 0
subway_name = ''
subway_id = ''

# 최상 5개 데이터 출력
for idx in range(5):

    # 행 데이터
    one = next(data)

    print(one)
    # 승차승객수 데이터
    in_num = one[4]

    # 승차 승객수 데이터 ',' 제거
    in_num_p1 = one[4].replace(',','')

    # 승차 승객수 정수 데이터 변경
    in_num_p2 = int(one[4].replace(',',''))

    #print(in_num, in_num_p1, in_num_p2)
    if in_num_p2 > max:
        max = in_num_p2
        subway_name = one[3]
        subway_id = one[2]

print('최다승차승객수: ', max)
print('지하철역 : ', subway_name)
print('역ID: ', subway_id)

