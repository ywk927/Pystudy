N = int(input())
T = int(input())
arr = list(map(int, input().split()))
numbers = list(map(int, input().split()))
i = 0
for number in numbers:
    i += number-1
    if i>= len(arr):
        i %= len(arr)
        print(arr[i], end=' ')
    else:
        print(arr[i], end=' ')
