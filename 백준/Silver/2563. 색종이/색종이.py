N = int(input())
arr = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, s+10):
        for j in range(e, e+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)