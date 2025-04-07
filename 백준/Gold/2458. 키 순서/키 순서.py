def recur(i):
    if graph[i]:
        for next_node in graph[i]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                path.append(next_node)
                recur(next_node)


def recur2(i):
    if graph_reverse[i]:
        for next_node in graph_reverse[i]:
            if visited2[next_node] == 0:
                visited2[next_node] = 1
                if next_node not in path:
                    path.append(next_node)
                path2.append(next_node)
                recur2(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
graph_reverse = [[] for _ in range(N+1)]
ans = 0
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph_reverse[e].append(s)
for i in range(1,N+1):
    visited = [0] * (N+1)
    path = [i]
    visited[i] = 1
    recur(i)
    visited2 = [0] * (N+1)
    path2 = [i]
    recur2(i)
    if len(path) == N:
        ans += 1
print(ans)


# visited = [0,0,0,0]
# graph = [[1,2,3]]
# for i in graph[0]:
#     print(visited[i])