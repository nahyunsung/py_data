# 최대값 구하기

# 1. 10-90 사이의 난수 20개를 기록한 리스트 nums 만들기
# 2. nums 리스트에서 최대갑 구하기

import random

nums = []

for x in range(20):
    r = random.randint(10, 90)
    nums.append(r)

print(nums)




max = 0
for x in range(20):
    if max < nums[x]:
        max = nums[x]
print(max)