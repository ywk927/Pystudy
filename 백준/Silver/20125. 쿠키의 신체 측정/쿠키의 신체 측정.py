N = int(input())
arr = [input() for _ in range(N)]
start_i = 0
start_j = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '*':
            cnt_idx = 0
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                if 0<=i+di<N and 0<j+dj<N and arr[i+di][j+dj] == '*':
                    cnt_idx += 1
                else:
                    break
            if cnt_idx == 4:
                start_i = i
                start_j = j
print(start_i+1, start_j+1)
# 방법 1
# 델타로 팔,허리 구하기
for di, dj in [[0,-1],[0,1],[1,0]]:
    cnt = 0
    for k in range(1,N):
        if 0<=start_i+di*k<N and 0<=start_j+dj*k<N and arr[start_i+di*k][start_j+dj*k] == '*':
            cnt += 1
        else:
            break
    print(cnt, end=' ')
# 다리구하기
cnt1 = 0
cnt2 = 0
for i in range(N-1,-1,-1):
    if arr[i][start_j-1] == '*':
        cnt1 += 1
    if cnt1 >= 1 and arr[i][start_j-1] == '_':
        print(cnt1, end=' ')
        break
for i in range(N-1, -1, -1):
    if arr[i][start_j+1] == '*':
        cnt2 += 1
    if cnt2 >= 1 and arr[i][start_j+1] == '_':
        print(cnt2)
        break

# 방법 2
# 하나씩 구하기
ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0
ans5 = 0
left = 1
while 0<=start_j-left and arr[start_i][start_j-left] == '*':
    ans1 += 1
    left += 1
right = 1
while start_j+right<N and arr[start_i][start_j+right] == '*':
    ans2 += 1
    right += 1
down = 1
while arr[start_i+down][start_j] == '*':
    ans3 += 1
    down += 1
down2 = 0
down3 = 0
while start_i+down+down2<N and arr[start_i+down+down2][start_j-1] == '*':
    ans4 += 1
    down2 += 1
while start_i+down+down3<N and arr[start_i+down+down3][start_j+1] == '*':
    ans5 += 1
    down3 += 1
print(ans1, ans2, ans3, ans4, ans5)
