T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    persons = N//10
    score_list = []
    for i in range(N):
        scores = list(map(int, input().split()))
        score = scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.2
        score_list.append(score)
    # print(score_list)
    my_student = score_list[K-1]
    score_list.sort(reverse=True)
    index = 1
    for i in range(N):
        if score_list[i] == my_student:
            index += i
    # print(index)
    if index <= persons:
        print(f'#{tc} A+')
    elif index <= persons*2:
        print(f'#{tc} A0')
    elif index <= persons*3:
        print(f'#{tc} A-')
    elif index <= persons*4:
        print(f'#{tc} B+')
    elif index <= persons*5:
        print(f'#{tc} B0')
    elif index <= persons*6:
        print(f'#{tc} B-')
    elif index <= persons*7:
        print(f'#{tc} C+')
    elif index <= persons*8:
        print(f'#{tc} C0')
    elif index <= persons*9:
        print(f'#{tc} C-')
    elif index <= persons*10:
        print(f'#{tc} D0')