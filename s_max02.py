# 최대값 구하기
# 20명의 [번호, 성적]데이터 중에 최고 성적을 받은 학새의 번호 구하기

import random as r

data = []
one = []

max = 0
num = 0

for x in range(20):
    grad = r.randint(0, 100)
    one.append(x+1)
    one.append(grad)
    data.append(one)
    one = []
print(data)

for x in data:
    if x[1] > max:
        max = x[1]
        num = x[0]

print('번호: ', num)
