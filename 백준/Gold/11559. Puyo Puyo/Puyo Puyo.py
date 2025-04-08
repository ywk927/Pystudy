arr = [list(input()) for _ in range(12)]
ans = 0
while True:
    # 한 번 쭉 돌았는데 터진게 없으면 while 문 종료하기 위한 변수 consecutive 생성
    consecutive = 0
    # 최하단 행부터 탐색해라
    for i in range(11,-1,-1):
        for j in range(6):
            # 연결되어 있는지 확인하기 위한 visited 생성
            visited = [[0] * 6 for _ in range(12)]
            # 뿌요에 해당하고 방문한 적이 없으면 탐색 시작
            if arr[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                q = [(i,j)]
                # bfs를 돌아라
                while q:
                    ti, tj = q.pop(0)
                    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ni, nj = ti + di, tj + dj
                        if 0<=ni<12 and 0<=nj<6 and arr[ni][nj] == arr[ti][tj] and visited[ni][nj] == 0:
                            visited[ni][nj] = visited[ti][tj] + 1
                            q.append((ni,nj))
                # 4개 이상이 연결되어 있는지 확인하기 위함
                cnt = 0
                change_idx = []
                for k in range(11,-1,-1):
                    for l in range(6):
                        # 사실 visited의 값은 중요하지 않고 방문했는지 안했는지를 확인하기 위함이므로 if visited != 0으로 조건문 설정
                        if visited[k][l] != 0:
                            cnt += 1
                            change_idx.append((k,l))
                if cnt >= 4:
                    # 터진다를 기록
                    consecutive += 1
                    for i, j in change_idx:
                        arr[i][j] = '.'
    # 한바퀴를 쭉 돌았다
    if consecutive >= 1:
        ans += 1
    # 터지지 않았으면 더 이상 터질게 없으므로 while 문 종료
    else:
        break

    # 아래로 끌어내리자
    for j in range(6):
        for i in range(11,-1,-1):
            # 만약 탐색 값이 color에 해당한다면
            if arr[i][j] != '.':
                # 일단 최하단 인덱스인 11번째 행에 넣을 수 있는지 확인하기 위해 f=11 인 변수 생성
                f = 11
                while arr[i][j] != '.' and f>=0:
                    # 만약 탐색한 값과 기준 인덱스 f와 같으면 이미 color가 있는 것이니 인덱스를 1 감소시키고 넘어가라
                    if f == i:
                        f -= 1
                        break
                    # 기준 인덱스가 비어있으면 거기에 추가하고 내 자리는 빈자리로 만들어라
                    if arr[f][j] == '.':
                        arr[f][j] = arr[i][j]
                        arr[i][j] = '.'
                    else:
                        f -= 1

print(ans)