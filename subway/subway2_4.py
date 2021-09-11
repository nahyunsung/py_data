import csv

f = open("2021년_8월_유무임별.csv")
data = csv.reader(f)

header = next(data)
print(header)

max_val = [0] *4
max_sta = [''] *4
nums = 0


for one in data:
    for i in range(4, 8):
        one[i] = int(one[i].replace(',',''))

    for x in range(4):
        if max_val[x] < one[4+x]:
            max_val[x] = one[4+x]
            max_sta[x] = one


for idx, one in enumerate(max_val):
    title = header[idx+4]
    value = format(one, ',')
    max_data = max_sta[idx]
    s_name = f'{max_data[3]} {max_data[1]}'
    print(title, s_name, f'{value}명')
