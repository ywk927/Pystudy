import heapq
N, M = map(int, input().split())
graph =[[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))
# print(graph)
visited = [float('inf') for _ in range(N+1)]
q = [(0,1)]
visited[1] = 0
while q:
    w, current = heapq.heappop(q)
    if w <= visited[current]:
        for next_w, next_e in graph[current]:
            new_w = w + next_w
            if new_w < visited[next_e]:
                visited[next_e] = new_w
                heapq.heappush(q, (new_w, next_e))
print(visited[N])