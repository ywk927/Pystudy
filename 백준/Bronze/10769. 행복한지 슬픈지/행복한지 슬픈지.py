arr = list(input())
N = len(arr)
i = 0
happy_cnt = 0
sad_cnt = 0
while i<N:
    if arr[i] == ':':
        if arr[i+1] == '-':
            if arr[i+2] == ')':
                happy_cnt += 1
                i += 3
            elif arr[i+2] == '(':
                sad_cnt += 1
                i += 3
            else:
                i += 3
        else:
            i += 2
    else:
        i += 1
if happy_cnt ==0 and sad_cnt ==0:
    print('none')
elif happy_cnt == sad_cnt:
    print('unsure')
elif happy_cnt > sad_cnt:
    print('happy')
else:
    print('sad')