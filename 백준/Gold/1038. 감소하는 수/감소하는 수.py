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
                if digit_index == 1:
                    z = ''
                    p = 1
                    for _ in range(1):
                        z = y[digits-p] + z
                        p += 1
                    b = 10-int(z)
                    i += b
                    break
                elif digit_index == 2:
                    z = ''
                    p = 1
                    for _ in range(2):
                        z = y[digits - p] + z
                        p += 1
                    b = 110-int(z)
                    i += b
                    break
                elif digit_index == 3:
                    z = ''
                    p = 1
                    for _ in range(3):
                        z = y[digits - p] + z
                        p += 1
                    b = 1210-int(z)
                    i += b
                    break
                elif digit_index == 4:
                    z = ''
                    p = 1
                    for _ in range(4):
                        z = y[digits - p] + z
                        p += 1
                    b = 13210 - int(z)
                    i += b
                    break
                elif digit_index == 5:
                    z = ''
                    p = 1
                    for _ in range(5):
                        z = y[digits - p] + z
                        p += 1
                    b = 143210 - int(z)
                    i += b
                    break
                elif digit_index == 6:
                    z = ''
                    p = 1
                    for _ in range(6):
                        z = y[digits - p] + z
                        p += 1
                    b = 1543210 - int(z)
                    i += b
                    break
                elif digit_index == 7:
                    z = ''
                    p = 1
                    for _ in range(7):
                        z = y[digits - p] + z
                        p += 1
                    b = 16543210 - int(z)
                    i += b
                    break
                elif digit_index == 8:
                    z = ''
                    p = 1
                    for _ in range(8):
                        z = y[digits - p] + z
                        p += 1
                    b = 176543210 - int(z)
                    i += b
                    break
                elif digit_index == 9:
                    z = ''
                    p = 1
                    for _ in range(9):
                        z = y[digits - p] + z
                        p += 1
                    b = 1876543210 - int(z)
                    i += b
                    break
                elif digit_index == 10:
                    z = ''
                    p = 1
                    for _ in range(10):
                        z = y[digits - p] + z
                        p += 1
                    b = 19876543210 - int(z)
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
