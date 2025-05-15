# N = int(input())
# arr = list(map(int, input().split()))
# cnt = 0
# k = N-1
# while k >= 1:
#     j = N-1
#     candidate = []
#     while j >= 1:
#         for i in range(N-1, -1, -1):
#             if j > i and arr[j] < arr[i]:
#                 candidate.append(arr[j])
#                 j -= 1
#                 break
#             if i == 0 and arr[j] >= arr[i]:
#                 j -= 1
#     if candidate:
#         candidate.sort()
#     else:
#         break
#     true_idx = False
#     for i in range(1, N):
#         for j in range(i):
#             if arr[i] != candidate[-1]:
#                 true_idx = True
#                 break
#         if true_idx and arr[i] == candidate[-1]:
#             arr = [arr[i]] + arr
#             arr.pop(i+1)
#             cnt += 1
#             break
#     k -= 1
# print(cnt)
import copy
N = int(input())
arr = list(map(int, input().split()))
cnt = 0
arr2 = copy.deepcopy(arr)
arr2.sort()
j = N-1
for i in range(N-1, -1, -1):
    if arr[i] == arr2[j]:
        cnt += 1
        j -= 1
print(N-cnt)