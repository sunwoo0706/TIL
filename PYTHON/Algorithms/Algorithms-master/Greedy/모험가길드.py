# 이것이 코딩테스트다

N = 5
arr = [2, 3, 1, 2, 2]

# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날수있음
# N명의 모험가에 대한 정보가 주어졌을때, 여행을 떠날 수 있는 그룹 수의 최대값


arr.sort()
print(arr)

count = 0
result = 0
for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0


print(result)
