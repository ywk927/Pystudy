# T= int(input())
# for tc in range(1,T+1):
#     N = int(input()) # 최대 백만개
#     prices = list(map(int, input().split()))
#     M = len(prices)
#     max_p = 0
#     start_idx = 0
#     max_idx = 0
#     ans = 0
#     while True:
#         if start_idx >= M:
#             break
#         else:
#             for i in range(start_idx, M):
#                 if prices[i] > max_p:
#                     max_p = prices[i]
#                     max_idx = i
#         if start_idx != max_idx:
#             for i in range(start_idx, max_idx):
#                ans += max_p-prices[i]
#             start_idx = max_idx + 1
#             max_p = 0
#         else:
#             break
#     print(ans)

T= int(input())
for tc in range(1,T+1):
    N = int(input()) # 최대 백만개
    prices = list(map(int, input().split()))
    M = len(prices)
    max_p = 0
    ans = 0
    for i in range(M-1,-1,-1):
        if max_p < prices[i]:
            max_p = prices[i]
        ans += max_p-prices[i]
    print(ans)