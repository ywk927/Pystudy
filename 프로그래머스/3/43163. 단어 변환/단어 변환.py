def solution(begin, target, words):
    answer = 0
    if target not in words:
        answer = 0
        return answer
    visited = [0] * len(words)
    q = [(begin, 0)]
    while q:
        prev, cnt = q.pop(0)
        if prev == target:
            answer = cnt
            break
        for j in range(len(words)):
            diff_idx = 0
            if visited[j] == 0:
                for i in range(len(begin)):
                    if prev[i] == words[j][i]:
                        diff_idx += 1
                if diff_idx == len(begin) - 1:
                    q.append((words[j], cnt+1))
                    visited[j] = 1
    return answer