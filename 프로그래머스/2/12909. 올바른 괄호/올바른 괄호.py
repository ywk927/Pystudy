def solution(s):
    answer = True
    open_cnt = 0
    for bracket in s:
        if open_cnt < 0:
            answer = False
            break
        if bracket == '(':
            open_cnt += 1
        else:
            open_cnt -= 1
    if open_cnt == 0:
        answer = True
    else:
        answer = False
    return answer