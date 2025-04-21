N = int(input())
if N == 1:
    print(0)
else:
    my = int(input())
    arr = []
    for _ in range(N-1):
        a = int(input())
        arr.append(a)
    total = False
    for i in range(N-1):
        if my > arr[i]:
            total = True
        else:
            total = False
            break
    my_cnt = 0
    if total:
        print(my_cnt)
    else:
        while True:
            true_index = False
            arr.sort(reverse=True)
            arr[0] -= 1
            my += 1
            my_cnt += 1
            for i in range(N-1):
                if arr[i] >= my:
                    true_index = False
                    break
                else:
                    true_index = True
            if true_index:
                print(my_cnt)
                break