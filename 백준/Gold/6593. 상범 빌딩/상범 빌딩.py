while True:
    L, R, C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break
    arr = [[] for _ in range(L)]
    for i in range(L):
        arr[i] = [list(input()) for _ in range(R)]
        blank = input()
    # print(arr)
    start_i = 0
    start_j = 0
    end_i = 0
    end_j = 0
    lev = 0
    lev_e = 0
    for l in range(L):
        for i in range(R):
            for j in range(C):
                if arr[l][i][j] == 'S':
                    lev, start_i, start_j = l, i, j
                if arr[l][i][j] == 'E':
                    lev_e, end_i, end_j = l, i, j
    q = [(lev, start_i, start_j)]
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    visited[lev][start_i][start_j] = 0
    while q:
        levels, ti, tj = q.pop(0)
        for di, dj, level in [[0,1,0],[1,0,0],[0,-1,0],[-1,0,0],[0,0,1], [0,0,-1]]:
            ni, nj, new_level = ti + di, tj + dj, levels+level
            if 0<=ni<R and 0<=nj<C and 0<=new_level<L and arr[new_level][ni][nj] != '#' and visited[new_level][ni][nj] == -1:
                visited[new_level][ni][nj] = visited[levels][ti][tj] + 1
                q.append((new_level,ni,nj))

        if visited[lev_e][end_i][end_j] != -1:
            break
    # print(visited)
    if visited[lev_e][end_i][end_j] == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {visited[lev_e][end_i][end_j]} minute(s).')