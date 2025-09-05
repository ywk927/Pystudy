from collections import deque

N = int(input())
A = list(map(str, input().split()))
B = list(map(str, input().split()))
M = int(input())
C = list(map(str, input().split()))

ans = []
candidate = deque([])
for i in range(N):
    if A[i] == '0':
        candidate.append(B[i])
candidate.reverse()
if candidate:
    for c in C:
        ans.append(candidate.popleft())
        candidate.append(c)
else:
    ans = C
print(*ans)