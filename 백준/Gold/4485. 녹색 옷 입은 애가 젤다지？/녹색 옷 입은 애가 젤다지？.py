import heapq

def dijkstra(start, end):
    dist = [[float('inf')]*N for _ in range(N)]
    dist[0][0] = arr[0][0]
    q = [(dist[0][0], 0, 0)]
    while q:
        w, i, j = heapq.heappop(q)
        if i == N-1 and j == N-1:
            return w
        else:
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N:
                    new_w = w + arr[ni][nj]
                    if new_w < dist[ni][nj]:
                        dist[ni][nj] = new_w
                        heapq.heappush(q, (new_w, ni, nj))
    return dist[N-1][N-1]

tc = 1
while True:
    N = int(input())
    if N ==0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(0,0)
    print(f'Problem {tc}: {result}')
    tc += 1