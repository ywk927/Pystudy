T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    t_num = data[0]
    heights = data[1:]

    lineup = []
    move_count = 0

    for h in heights:
        i = len(lineup)
        lineup.append(h)
        # 삽입 정렬처럼 오른쪽에서 왼쪽으로 이동
        while i > 0 and lineup[i - 1] > lineup[i]:
            lineup[i - 1], lineup[i] = lineup[i], lineup[i - 1]
            move_count += 1
            i -= 1

    print(t_num, move_count)
