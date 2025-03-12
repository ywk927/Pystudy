width, height = map(int, input().split())
N = int(input())
max_area = 0
width_idx = []
height_idx = []
for _ in range(N):
    whether_w_h, idx = map(int,input().split())
    if whether_w_h == 0:
        height_idx.append(idx)
    elif whether_w_h == 1:
        width_idx.append(idx)
if width_idx:
    width_idx.sort()
    a = width_idx[-1]
    new_width_idx = [0] * (N+1)
    new_width_idx[0] = width_idx[0]
    for i in range(1, len(width_idx)):
        new_width_idx[i] = width_idx[i] - width_idx[i - 1]
    new_width_idx.append(width - a)
if height_idx:
    height_idx.sort()
    b = height_idx[-1]
    new_height_idx = [0] * (N+1)
    new_height_idx[0] = height_idx[0]
    for i in range(1, len(height_idx)):
        new_height_idx[i] = height_idx[i] - height_idx[i - 1]
    new_height_idx.append(height - b)

if width_idx and height_idx:
    for i in range(len(new_width_idx)):
        for j in range(len(new_height_idx)):
            area = new_width_idx[i] * new_height_idx[j]
            if max_area < area:
                max_area = area
elif height_idx == [] and width_idx == []:
    max_area = height * width
elif height_idx == []:
    for i in range(len(new_width_idx)):
        area = new_width_idx[i] * height
        if max_area < area:
            max_area = area
elif width_idx == []:
    for i in range(len(new_height_idx)):
        area = new_height_idx[i] * width
        if max_area < area:
            max_area = area
print(max_area)