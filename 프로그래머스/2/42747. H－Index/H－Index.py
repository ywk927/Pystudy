def solution(citations):
    answer = 0
    n = len(citations)
    i = n
    while i > 0:
        cnt_idx = 0
        for k in citations:
            if k >= i:
                cnt_idx += 1
        if cnt_idx >= i and n-cnt_idx <= i:
            answer = i
            break
        else:
            i -= 1
    return answer