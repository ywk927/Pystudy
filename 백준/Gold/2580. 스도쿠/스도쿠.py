def check(i,j):
    for k in range(9):
        if k != i and arr[k][j] == arr[i][j]:
            return False
        if k != j and arr[i][k] == arr[i][j]:
            return False
    # for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
    #     for k in range(1,9):
    #         ni, nj = i + di*k, j + dj*k
    #         if 0<=ni<9 and 0<=nj<9:
    #             if arr[ni][nj] == 0:
    #                 continue
    #             if arr[i][j] == arr[ni][nj]:
    #                 return False
    #         else:
    #             break
    si, sj = (i//3) * 3, (j//3) * 3
    for u in range(si, si+3):
        for v in range(sj,sj+3):
            if (u,v) != (i,j) and arr[u][v] == arr[i][j]:
                return False
    return True
    # if i<=2 and j<=2:
    #     for u in range(3):
    #         for v in range(3):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif 2<i<=5 and j<=2:
    #     for u in range(3,6):
    #         for v in range(3):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif 5<i<=8 and j<=2:
    #     for u in range(6,9):
    #         for v in range(3):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif i<=2 and 2<j<=5:
    #     for u in range(3):
    #         for v in range(3,6):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif 2<i<=5 and 2<j<=5:
    #     for u in range(3,6):
    #         for v in range(3,6):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif 5<i<=8 and 2<j<=5:
    #     for u in range(6,9):
    #         for v in range(3,6):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif i<=2 and 5<j<=8:
    #     for u in range(3):
    #         for v in range(6,9):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif 2<i<=5 and 5<j<=8:
    #     for u in range(3,6):
    #         for v in range(6,9):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # elif 5<i<=8 and 5<j<=8:
    #     for u in range(6,9):
    #         for v in range(6,9):
    #             if u == i and v == j:
    #                 continue
    #             if arr[i][j] == arr[u][v]:
    #                 return False
    # return True


def f(x):
    global found
    if x == cnt:
        for i in range(9):
            print(*arr[i])
        found = True
        return
    if found:
        return

    i, j = zero_list[x][0], zero_list[x][1]
    for k in range(1,10):
        arr[i][j] = k
        if check(i,j):
            f(x+1)
            if found:
                return
        arr[i][j] = 0


# ans = 0
arr = [list(map(int, input().split())) for _ in range(9)]
cnt = 0
zero_list = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero_list.append((i,j))
            cnt += 1
found = False
f(0)

