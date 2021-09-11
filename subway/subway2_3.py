import csv

f = open("2021년_8월_유무임별.csv")
data = csv.reader(f)

header = next(data)
print(header)

max = 0
max_data = ""

for one in data:
    for i in range(4, 8):
        one[i] = int(one[i].replace(",",''))
    nums = one[4]+one[6]
    if one[6] != 0 and nums > 100000:
        rate = one[4] / (one[4]+ one[6])
        if max < rate:
            max = rate
            max_data = one


print(max)
print(max_data)