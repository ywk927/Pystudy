# 6 by 6의 경우 4*4 만 보면 된다
# 그 안에서 서로 다른 3개의 점을 선택하자

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
candidate = []
for i in range(1,N-1):
    for j in range(1,N-1):
        candidate.append([i,j])
b = len(candidate)
min_ans = float('inf')
visited = [[0] * N for _ in range(N)]
possible_ans = 0
for i in range(b):
    for j in range(b):
        for k in range(b):
            if i != j and j != k and i != k:
                cnt = 0
                c1 = candidate[i][0]
                c2 = candidate[i][1]
                visited[c1][c2] = 1
                possible_ans += arr[c1][c2]
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    if visited[c1+di][c2+dj] == 0:
                        cnt += 1
                        visited[c1+di][c2+dj] = 1
                        possible_ans += arr[c1+di][c2+dj]
                c3 = candidate[j][0]
                c4 = candidate[j][1]
                visited[c3][c4] = 1
                possible_ans += arr[c3][c4]
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if visited[c3 + di][c4 + dj] == 0:
                        cnt += 1
                        visited[c3 + di][c4 + dj] = 1
                        possible_ans += arr[c3 + di][c4 + dj]
                c5 = candidate[k][0]
                c6 = candidate[k][1]
                visited[c5][c6] = 1
                possible_ans += arr[c5][c6]
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if visited[c5 + di][c6 + dj] == 0:
                        cnt += 1
                        visited[c5 + di][c6 + dj] = 1
                        possible_ans += arr[c5 + di][c6 + dj]
                if cnt == 12:
                    min_ans = min(min_ans, possible_ans)
                possible_ans = 0
                visited = [[0] * N for _ in range(N)]
print(min_ans)