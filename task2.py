res = list(map(int, input().split()))
new = []
for i in res:
    new.append(res[i-2])
print(new)