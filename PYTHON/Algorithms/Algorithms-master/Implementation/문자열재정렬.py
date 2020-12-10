s = list('K1KA5CB7')

result = []
n = 0
for i in range(len(s)):
    if s[i].isdigit():
        n += int(s[i])
    else:
        result.append(s[i])
result.sort()
if n != 0:
    result.append(str(n))
result = ''.join(result)
print(result)
