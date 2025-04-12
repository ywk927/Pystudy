arr = list(input())
# ()이 바로 나오면 이건 레이저
# ( 다음에 또 (이 나오면 파이프가 추가됐다는 의미
# 레이저가 발사되면 파이프 개수만큼 추가해주면 됨
N = len(arr)
pipe_cnt = 0
ans = 0
i = 0
while i<N:
    if arr[i] == '(':
        # 마지막에는 무조건 닫는 괄호가 나와서 인덱스 에러 신경안써도 될듯
        if arr[i+1] == ')':
            ans += pipe_cnt
            i += 2
        else:
            pipe_cnt += 1
            i += 1
    else:
        pipe_cnt -= 1
        ans += 1
        i += 1
print(ans)