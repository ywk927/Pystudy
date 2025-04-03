N = int(input())
arr = [list(input()) for _ in range(N)]
width_cnt = 0
height_cnt = 0
cnt = 0
cnt2 = 0
for i in range(N):
    cnt = 0
    cnt2 = 0
    j = 0
    k = 0
    while j <= N-1:
        if cnt == 2:
            width_cnt += 1
            while True:
                if arr[i][j] == '.':
                    j += 1
                    if j == N:
                        break
                elif arr[i][j] == 'X':
                    break
            cnt = 0
        if j == N:
            break
        if arr[i][j] == '.':
            cnt += 1
            j += 1
        elif arr[i][j] == 'X':
            cnt = 0
            j += 1
    while k <= N-1:
        if cnt2 == 2:
            height_cnt += 1
            while True:
                if arr[k][i] == '.':
                    k += 1
                    if k == N:
                        break
                elif arr[k][i] == 'X':
                    break
            cnt2 = 0
        if k == N:
            break
        if arr[k][i] == '.':
            cnt2 += 1
            k += 1
        elif arr[k][i] == 'X':
            cnt2 = 0
            k += 1
    if cnt == 2:
        width_cnt += 1
    if cnt2 == 2:
        height_cnt += 1
print(width_cnt, height_cnt)