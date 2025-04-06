from collections import deque
wheel1 = list(input())
wheel2 = list(input())
wheel3 = list(input())
wheel4 = list(input())
wheel1_deque = deque(wheel1)
wheel2_deque = deque(wheel2)
wheel3_deque = deque(wheel3)
wheel4_deque = deque(wheel4)

wheels_list = [0,1,2,3,4]
K = int(input())
for _ in range(K):
    wheel_num, direction = map(int, input().split())
    # 리스트가 변화하는 것에 영향을 받지 않기 위해 여기서 새로운 변수로 기록해줌
    w2, x1, x2, y1, y2, z1 = wheel1_deque[2], wheel2_deque[6], wheel2_deque[2], wheel3_deque[6], wheel3_deque[2], wheel4_deque[6]
    # 해당 톱니바퀴부터 바꿔주면 뒤에 영향 x
    # 근데 이렇게 하면 고려할 요소가 너무 많아짐 -> 따라서 위와 같이 새로운 변수를 기록하는 방법으로 바꿈
    # if wheel_num == 1:
    #     if wheel1_deque[2] != wheel2_deque[6]:
    #         if direction == -1:
    #             wheel1_deque.append(wheel1_deque[0])
    #             wheel1_deque.popleft()
    #         else:
    #             wheel1_deque.appendleft(wheel1_deque[-1])
    #             wheel1_deque.pop()
    #         # 1번은 업데이트 완료
    #         # 2,3번이 같다면
    #         if wheel2_deque[2] == wheel3_deque[6]:
    #             if direction == -1:
    #                 wheel2_deque.appendleft(wheel2_deque[-1])
    #                 wheel2_deque.pop()
    #             else:
    #                 wheel2_deque.append(wheel2_deque[0])
    #                 wheel2_deque.popleft()
    #         # 1번 2번 3번이 다르고 3번과 4번이 같으면
    #         elif wheel2_deque[2] != wheel3_deque[6] and wheel3_deque[2] == wheel4_deque[6]:
    #             if direction == -1:
    #                 wheel2_deque.appendleft(wheel2_deque[-1])
    #                 wheel2_deque.pop()
    #                 wheel3_deque.append(wheel3_deque[0])
    #                 wheel3_deque.popleft()
    #             else:
    #                 wheel2_deque.append(wheel2_deque[0])
    #                 wheel2_deque.popleft()
    #                 wheel3_deque.appendleft(wheel3_deque[-1])
    #                 wheel3_deque.pop()
    #         elif wheel2_deque[2] != wheel3_deque[6] and wheel3_deque[2] != wheel4_deque[6]:
    #             if direction == -1:
    #                 wheel2_deque.appendleft(wheel2_deque[-1])
    #                 wheel2_deque.pop()
    #                 wheel3_deque.append(wheel3_deque[0])
    #                 wheel3_deque.popleft()
    #                 wheel4_deque.appendleft(wheel4_deque[-1])
    #                 wheel4_deque.pop()
    #             else:
    #                 wheel2_deque.append(wheel2_deque[0])
    #                 wheel2_deque.popleft()
    #                 wheel3_deque.appendleft(wheel3_deque[-1])
    #                 wheel3_deque.pop()
    #                 wheel4_deque.append(wheel4_deque[0])
    #                 wheel4_deque.popleft()
    #     # 1번과 2번이 같다면
    #     else:
    #         if direction == -1:
    #             wheel1_deque.append(wheel1_deque[0])
    #             wheel1_deque.popleft()
    #         else:
    #             wheel1_deque.appendleft(wheel1_deque[-1])
    #             wheel1_deque.pop()
    if wheel_num == 1:
        if direction == -1:
            wheel1_deque.append(wheel1_deque[0])
            wheel1_deque.popleft()
        else:
            wheel1_deque.appendleft(wheel1_deque[-1])
            wheel1_deque.pop()
        if w2 != x1:
            if direction == -1:
                wheel2_deque.appendleft(wheel2_deque[-1])
                wheel2_deque.pop()
            else:
                wheel2_deque.append(wheel2_deque[0])
                wheel2_deque.popleft()
            if x2 != y1:
                if direction == -1:
                    wheel3_deque.append(wheel3_deque[0])
                    wheel3_deque.popleft()
                else:
                    wheel3_deque.appendleft(wheel3_deque[-1])
                    wheel3_deque.pop()
                if y2 != z1:
                    if direction == -1:
                        wheel4_deque.appendleft(wheel4_deque[-1])
                        wheel4_deque.pop()
                    else:
                        wheel4_deque.append(wheel4_deque[0])
                        wheel4_deque.popleft()
    elif wheel_num == 4:
        if direction == -1:
            wheel4_deque.append(wheel4_deque[0])
            wheel4_deque.popleft()
        else:
            wheel4_deque.appendleft(wheel4_deque[-1])
            wheel4_deque.pop()
        if z1 != y2:
            if direction == -1:
                wheel3_deque.appendleft(wheel3_deque[-1])
                wheel3_deque.pop()
            else:
                wheel3_deque.append(wheel3_deque[0])
                wheel3_deque.popleft()
            if x2 != y1:
                if direction == -1:
                    wheel2_deque.append(wheel2_deque[0])
                    wheel2_deque.popleft()
                else:
                    wheel2_deque.appendleft(wheel2_deque[-1])
                    wheel2_deque.pop()
                if w2 != x1:
                    if direction == -1:
                        wheel1_deque.appendleft(wheel1_deque[-1])
                        wheel1_deque.pop()
                    else:
                        wheel1_deque.append(wheel1_deque[0])
                        wheel1_deque.popleft()
    elif wheel_num == 2:
        if direction == -1:
            wheel2_deque.append(wheel2_deque[0])
            wheel2_deque.popleft()
        else:
            wheel2_deque.appendleft(wheel2_deque[-1])
            wheel2_deque.pop()
        if w2 != x1:
            if direction == -1:
                wheel1_deque.appendleft(wheel1_deque[-1])
                wheel1_deque.pop()
            else:
                wheel1_deque.append(wheel1_deque[0])
                wheel1_deque.popleft()
        if x2 != y1:
            if direction == -1:
                wheel3_deque.appendleft(wheel3_deque[-1])
                wheel3_deque.pop()
            else:
                wheel3_deque.append(wheel3_deque[0])
                wheel3_deque.popleft()
            if y2 != z1:
                if direction == -1:
                    wheel4_deque.append(wheel4_deque[0])
                    wheel4_deque.popleft()
                else:
                    wheel4_deque.appendleft(wheel4_deque[-1])
                    wheel4_deque.pop()
    elif wheel_num == 3:
        if direction == -1:
            wheel3_deque.append(wheel3_deque[0])
            wheel3_deque.popleft()
        else:
            wheel3_deque.appendleft(wheel3_deque[-1])
            wheel3_deque.pop()
        if y2 != z1:
            if direction == -1:
                wheel4_deque.appendleft(wheel4_deque[-1])
                wheel4_deque.pop()
            else:
                wheel4_deque.append(wheel4_deque[0])
                wheel4_deque.popleft()
        if x2 != y1:
            if direction == -1:
                wheel2_deque.appendleft(wheel2_deque[-1])
                wheel2_deque.pop()
            else:
                wheel2_deque.append(wheel2_deque[0])
                wheel2_deque.popleft()
            if w2 != x1:
                if direction == -1:
                    wheel1_deque.append(wheel1_deque[0])
                    wheel1_deque.popleft()
                else:
                    wheel1_deque.appendleft(wheel1_deque[-1])
                    wheel1_deque.pop()
ans = 0
if wheel1_deque[0] == '1':
    ans += 1
if wheel2_deque[0] == '1':
    ans += 2
if wheel3_deque[0] == '1':
    ans += 4
if wheel4_deque[0] == '1':
    ans += 8

print(ans)