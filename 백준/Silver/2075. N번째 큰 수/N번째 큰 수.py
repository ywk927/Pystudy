import heapq

N = int(input())
q = []

for i in range(N):
    row = list(map(int, input().split()))
    for num in row:
        heapq.heappush(q, num)
        if len(q) > N:
            heapq.heappop(q)
print(q[0])