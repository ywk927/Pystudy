import copy

def recur(i,N,used):
    if i == N:
        if candidate not in candidates:
            candidates.append(candidate.copy())
        return
    for j in range(len(path)):
        if used[j] == 0:
            candidate.append(path[j])
            used[j] = 1
            recur(i+1, N, used)
            used[j] = 0
            candidate.pop()

        
def is_prime(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True
        
    
candidate = []
candidates = []
path = []

def solution(numbers):
    answer = 0
    N = len(numbers)
    used = [0] * N
    for num in numbers:
        path.append(num)
    for i in range(1,N+1):
        recur(0,i,used)
    int_nums = []
    for number in candidates:
        new_num = ''.join(number)
        if int(new_num) not in int_nums:
            int_nums.append(int(new_num))
    for nums in int_nums:
        if is_prime(nums):
            answer += 1
    return answer