def combination(i, start):
    if i == 6:
        print(*path)
        return
    else:
        for j in range(start, N):
            if used[j] == 0:
                path.append(arr[j])
                used[j] = 1
                combination(i+1, j)
                used[j] = 0
                path.pop()

while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    k = arr[0]
    arr.pop(0)
    N = len(arr)
    path = []
    used = [0] * N
    combination(0,0)
    print()