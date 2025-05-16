import heapq
N = int(input())
presents = []
for _ in range(N):
    arr = list(map(int, input().split()))
    if arr == [0]:
        if presents:
            ans = -heapq.heappop(presents)
            print(ans)
        else:
            print(-1)
    else:
        for i in range(1, len(arr)):
            heapq.heappush(presents, -arr[i])
