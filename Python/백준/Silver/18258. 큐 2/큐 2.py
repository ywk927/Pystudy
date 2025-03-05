import sys
input = sys.stdin.readline

queue = [0] * 2000000
front = rear = -1

n = int(input())
for _ in range(n):
    order = input().rstrip()
    if order[:4] == 'push':
        a, x = order.split()
        x = int(x)
        rear += 1
        queue[rear] = x
    elif order == 'pop':
        if front == rear:
            print(-1)
        else:
            front += 1
            print(queue[front])
    elif order == 'size':
        print(rear - front)
    elif order == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if front == rear:
            print(-1)
        else:
            front += 1
            print(queue[front])
            front -= 1
    else:
        if front == rear:
            print(-1)
        else:
            print(queue[rear])
