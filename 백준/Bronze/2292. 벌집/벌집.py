N = int(input())
ans = 1
if N == 1:
    print(ans)
else:
    i = 1
    j = 6
    while True:
        i += j
        ans += 1
        if i >= N:
            print(ans)
            break
        j += 6
