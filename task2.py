n = int(input())
res = list(map(int, input().split()))


if len(res) != n:
    print("Введено неверное количество чисел!")
    exit()
 

new = [res[-1]]  
new.extend(res[:-1])  
print(*new)

