N = int(input())
arr = list(map(int, input().split()))
min = 1000001
max = -1000001
for num in arr:
    if min > num:
        min = num
    if max < num:
        max = num
print(min, max)