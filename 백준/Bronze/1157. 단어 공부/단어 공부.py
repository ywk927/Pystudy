arr = input()
words = [0] * 26
for i in arr:
    i = i.upper()
    words[ord(i)-65] += 1
max_cnt = 0
cnt_idx = 0
max_idx = -1
for idx in range(26):
    if max_cnt < words[idx]:
        cnt_idx = 1
        max_cnt = words[idx]
        max_idx = idx
    elif max_cnt == words[idx]:
        cnt_idx = 2
if cnt_idx == 1:
    print(chr(65+max_idx))
else:
    print('?')