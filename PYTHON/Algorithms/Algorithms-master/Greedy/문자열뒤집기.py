# 이것이 코딩테스트다
# https://www.acmicpc.net/problem/1439

# 문자열 뒤집어서 문자열 s에 있는 모든 숫자를 전부 같게만들기

arr = list('0001100')
# s = str(input())

# 연속된 문자열만 뒤집을 수 있음

arr = input()

count0, count1 = 0, 0

if arr[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(arr) - 1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))