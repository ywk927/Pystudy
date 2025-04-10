for tc in range(1,11):
    T = int(input())
    arr = [list(input()) for _ in range(16)]
    q= []
    end = []
    visited = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                visited[i][j] = 1
                q.append((i,j))
            elif arr[i][j] == '3':
                end.append(i)
                end.append(j)
    while q:
        ti, tj = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] != '1' and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni,nj))
    if visited[end[0]][end[1]] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')