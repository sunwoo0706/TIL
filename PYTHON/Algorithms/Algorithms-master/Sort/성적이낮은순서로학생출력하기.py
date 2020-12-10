n = int(input())

arr = []
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

arr.sort(key=lambda x: x[1], reverse=True)


for n, s in arr:
    print(n, end=' ')