from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 추가되는 양분
nutri = [[5] * N for _ in range(N)]                      # 현재 양분
trees = [[deque() for _ in range(N)] for _ in range(N)]  # 각 칸의 나무 나이

# 초기 나무 배치
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

# 초기에는 오름차순으로 맞춰두면 봄 처리에 유리
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            trees[i][j] = deque(sorted(trees[i][j]))

dirs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

for _ in range(K):
    # 봄 & 여름
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            alive = deque()
            dead_feed = 0
            # 어린 나무부터 양분 먹게(오름차순)
            while trees[i][j]:
                age = trees[i][j].popleft()
                if nutri[i][j] >= age:
                    nutri[i][j] -= age
                    alive.append(age + 1)  # 한 살 먹음
                else:
                    dead_feed += age // 2  # 여름에 양분으로
            trees[i][j] = alive
            nutri[i][j] += dead_feed

    # 가을: 번식 (나이 % 5 == 0 인 나무가 주변 8칸에 나이 1 나무 번식)
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            for age in trees[i][j]:
                if age % 5 == 0:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            trees[ni][nj].appendleft(1)  # 어린 나무가 앞쪽(어린 순)으로

    # 겨울: 양분 추가
    for i in range(N):
        for j in range(N):
            nutri[i][j] += A[i][j]

ans = sum(len(trees[i][j]) for i in range(N) for j in range(N))
print(ans)