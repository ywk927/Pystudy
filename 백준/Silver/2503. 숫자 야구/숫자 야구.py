N = int(input())
arr = []
for _ in range(N):
    num, s, b = map(int, input().split())
    arr.append([num, s, b])
cnt = 0
for num in range(123,988):
    str_num = str(num) # 영수의 가능한 숫자
    if len(set(str_num)) == 3 and '0' not in str_num:
        is_valid = True
        for number, s, b in arr:
            str_number = str(number) # 부른 숫자
            s2 = 0
            b2 = 0
            for i in range(3):
                if str_num[i] == str_number[i]:
                    s2 += 1
                elif str_num[i] in str_number:
                    b2 += 1
            if s != s2 or b != b2:
                is_valid = False
                break
        if is_valid:
            cnt += 1
print(cnt)
