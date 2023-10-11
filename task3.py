m = int(input())
n = int(input())
weights = []
for i in range(n):
    wei = int(input())
    weights.append(wei)

# Сортировка массива весов
weights.sort()

# Перевозка рыбаков
boats = 0
left = 0
right = n - 1
while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boats += 1

print(boats)