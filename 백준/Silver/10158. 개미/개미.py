x ,y = map(int, input().split())
i ,j = map(int, input().split())
t = int(input())
idx = (t+i) % x
idx_i = (t+i) // x
if idx_i % 2 == 1:
    print(x-idx, end = ' ')
else:
    print(idx, end = ' ')
idx2 = (t+j) % y
idx_j = (t+j) // y
if idx_j % 2 == 1:
    print(y-idx2)
else:
    print(idx2)