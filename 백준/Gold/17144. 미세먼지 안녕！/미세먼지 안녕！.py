import copy
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
copied_arr = copy.deepcopy(arr)
cleaner1 = [0,0]
cleaner2 = [0,0]
for i in range(N):
    if arr[i][0] == -1:
        cleaner1 = [i,0]
        break
cleaner2 = [cleaner1[0]+1, 0]

# 까꾸로 돌자
direction_idx1 = 0
direction1 = [[-1,0],[0,1],[1,0],[0,-1]]
direction_idx2 = 0
direction2 = [[1,0],[0,1],[-1,0],[0,-1]]

for _ in range(T):
    for i in range(N):
        for j in range(M):
            if copied_arr[i][j] != -1 and copied_arr[i][j] != 0:
                disperse = copied_arr[i][j]//5 # 뒤에서 하면 값이 변경됨 + 영향을 미치지 않게 하기 위해
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    ni, nj = i+di, j+ dj
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] != -1:
                        arr[ni][nj] += disperse
                        arr[i][j] -= disperse
    up = cleaner1[0]
    for i in range(up-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for i in range(M-1):
        arr[0][i] = arr[0][i+1]
    for i in range(up):
        arr[i][M-1] = arr[i+1][M-1]
    for i in range(M-1, 1,-1):
        arr[up][i] = arr[up][i-1]
    arr[up][1] = 0

    down = cleaner2[0]
    for i in range(down + 1, N - 1):
        arr[i][0] = arr[i + 1][0]
    for i in range(M - 1):
        arr[N - 1][i] = arr[N - 1][i + 1]
    for i in range(N - 1, down, -1):
        arr[i][M - 1] = arr[i - 1][M - 1]
    for i in range(M - 1, 1, -1):
        arr[down][i] = arr[down][i - 1]
    arr[down][1] = 0
    copied_arr = copy.deepcopy(arr)

result  = 2 # 공기청정기 -2 생각
for i in range(N):
    for j in range(M):
        result += arr[i][j]

print(result)