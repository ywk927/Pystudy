N = int(input())
arr = list(map(int, input().split()))
students = [0] * N
for i in range(N):
    j = i - arr[i]
    if i > j:
        for k in range(i-1, j-1, -1):
            students[k+1] = students[k]
    students[j] = i+1
print(*students)