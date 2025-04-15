N = int(input())
cnt = 9
i = 10
if N<10:
    for i in range(10):
        if i == N:
            print(i)
if N>=10:
    while True:
        j = i
        ans = i
        cnt_index = False
        f = j
        y = str(i)
        digits = 1
        while f >= 10:
            f //= 10
            digits += 1
        digit_index = 0
        find_index = False
        while j >= 10:
            digit_index += 1
            k = j
            a = k % 10
            k //= 10
            k %= 10
            j //= 10
            if k > a:
                cnt_index = True
            else:
                find_index = True
                cnt_index = False
                # digit_list = [[],[10],[110],[1210],[13210],[143210],[1543210],[16543210],[176543210],[1876543210],[19876543210]]
                digit_list = [0, 10, 110, 1210, 13210, 143210, 1543210, 16543210, 176543210, 1876543210, 19876543210]

                z = ''
                p = 1
                for _ in range(digit_index):
                    z = y[digits - p] + z
                    p += 1
                b = digit_list[digit_index] - int(z)
                i += b
                break

        if cnt_index == True:
            cnt += 1
        if cnt == N:
            print(ans)
            break
        if not find_index:
            i += 1
        if i > 9876543210:
            print(-1)
            break
