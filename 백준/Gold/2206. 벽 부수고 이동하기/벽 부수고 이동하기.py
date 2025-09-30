# 2206
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
# print(visited)
chk = False
directions = [(0,1), (1,0), (0,-1), (-1,0)]
i, j = 0, 0
if arr[i][j] == '0' and visited[0][i][j] == 0:
    visited[0][i][j] = 1
    q = deque([(i, j, 0, 1)])
    while q:
        ti, tj, breaks, cnt = q.popleft()
        if ti == N-1 and tj == M-1:
            chk = True
            print(cnt)
            break
        for di, dj in directions:
            ni, nj = ti + di, tj + dj
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == '0' and visited[breaks][ni][nj] == 0:
                    visited[breaks][ni][nj] = 1
                    q.append((ni, nj, breaks, cnt + 1))
                elif arr[ni][nj] == '1' and visited[breaks][ni][nj] == 0:
                    if breaks == 0:
                        visited[1][ni][nj] = 1
                        q.append((ni, nj, 1, cnt + 1))
if not chk:
    print(-1)