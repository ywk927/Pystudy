from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
total_cheese = 10  # 랜덤숫자
time = 0

while total_cheese != 0:
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((0,0))
    visited[0][0] = 1
    melt_cheese = []
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                if arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                elif arr[ni][nj] == 1:
                    visited[ni][nj] = 1
                    melt_cheese.append((ni,nj))
    time += 1
    last_cheese = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                last_cheese += 1
    for x, y in melt_cheese:
        arr[x][y] = 0
    total_cheese = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                total_cheese += 1
    if total_cheese == 0:
        print(time)
        print(last_cheese)