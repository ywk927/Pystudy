# from pprint import pprint
arr = [list(input()) for _ in range(12)]
ans = 0
while True:
    consecutive = 0
    for i in range(11,-1,-1):
        for j in range(6):
            visited = [[0] * 6 for _ in range(12)]
            if arr[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                q = [(i,j)]
                while q:
                    ti, tj = q.pop(0)
                    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ni, nj = ti + di, tj + dj
                        if 0<=ni<12 and 0<=nj<6 and arr[ni][nj] == arr[ti][tj] and visited[ni][nj] == 0:
                            visited[ni][nj] = visited[ti][tj] + 1
                            q.append((ni,nj))
                cnt = 0
                change_idx = []
                for k in range(11,-1,-1):
                    for l in range(6):
                        if visited[k][l] != 0:
                            cnt += 1
                            change_idx.append((k,l))
                if cnt >= 4:
                    consecutive += 1
                    for i, j in change_idx:
                        arr[i][j] = '.'
    if consecutive >= 1:
        ans += 1
    else:
        break

    # for j in range(6):
    #     i = 11
    #     idx_find = True
    #     while idx_find and i>=0:
    #         idx_find = False
    #         if arr[i][j] == '.':
    #             idx_find = True
    #             i -= 1
    #     f = 11
    #     for k in range(i,-1,-1):
    #         arr[k][j] = arr[f][j]
    # for j in range(6):
    #     cnt2 = 0
    #     f = 11
    #     for i in range(11,-1,-1):
    #         if arr[i][j] == '.':
    #             cnt2 += 1
    #         else:
    #             if cnt2:
    #                 for _ in range(cnt2):
    #                     arr[f][j] = arr[i][j]
    #                     arr[i][j] = '.'
    #                     f -= 1
    #             else:
    #                 f -= 1
    for j in range(6):
        for i in range(11,-1,-1):
            if arr[i][j] != '.':
                f = 11
                while arr[i][j] != '.' and f>=0:
                    if f == i:
                        f -= 1
                        break
                    if arr[f][j] == '.':
                        arr[f][j] = arr[i][j]
                        arr[i][j] = '.'
                    else:
                        f -= 1
    # print(arr)


# pprint(arr)
print(ans)