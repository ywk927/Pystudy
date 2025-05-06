import heapq
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))
start = 1
max_ans = 0
while start <= N:
    q = [(0,start)]
    visited1 = [float('inf') for _ in range(N+1)]
    visited1[start] = 0
    while q:
        w, current = heapq.heappop(q)
        if current == X:
            break
        if w <= visited1[current]:
            for next_w, next_e in graph[current]:
                new_w = w + next_w
                if new_w < visited1[next_e]:
                    visited1[next_e] = new_w
                    heapq.heappush(q, (new_w, next_e))
    one_way = visited1[X]
    # print(one_way)
    q = [(0,X)]
    # print(q)
    visited2 = [float('inf') for _ in range(N+1)]
    visited2[X] = 0
    while q:
        w, current = heapq.heappop(q)
        if current == start:
            break
        if w <= visited2[current]:
            for next_w, next_e in graph[current]:
                new_w = w + next_w
                if new_w < visited2[next_e]:
                    visited2[next_e] = new_w
                    heapq.heappush(q, (new_w, next_e))
    way_back = visited2[start]
    # print(way_back)
    ans = one_way+way_back
    max_ans = max(max_ans, ans)
    start += 1
print(max_ans)
