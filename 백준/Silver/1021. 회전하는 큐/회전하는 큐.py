N, M = map(int, input().split())
print_list = list(map(int, input().split()))
arr = [i for i in range(1,N+1)]
cnt = 0
x = 0
while True:
    if print_list[x] == arr[0]:
        arr.pop(0)
        x += 1
        if x == M:
            break
    else:
        idx = arr.index(print_list[x])
        if idx <= len(arr)//2:
            arr.append(arr[0])
            arr.pop(0)
            cnt += 1
        else:
            arr = [arr[len(arr)-1]] + arr
            arr.pop()
            cnt += 1
print(cnt)