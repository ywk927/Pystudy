from collections import deque
N = int(input())
cnt = 0
arr = deque()
for i in range(1, N+1):
    arr.append(i)
while True:
    if cnt == N-1:
        break
    arr.popleft()
    cnt += 1
    # print(arr[0])
    arr.append(arr[0])
    arr.popleft()
print(arr[0])