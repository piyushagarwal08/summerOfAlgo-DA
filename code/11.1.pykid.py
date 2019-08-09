s = input()
result = []
for i in s:
    if len(result) == 0:
        result.append(i)
    elif i != result[-1]:
        result.append(i)
    else:
        result.remove(i)

for i in result:
    print(i,end="")

