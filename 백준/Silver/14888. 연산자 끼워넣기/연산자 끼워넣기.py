def f(i,operation,op1,op2,op3,op4):
    # global cnt
    # cnt += 1
    global max_result, min_result
    if op1<0 or op2<0 or op3<0 or op4<0:
        return
    if i == N:
        if max_result < operation:
            max_result = operation
        if min_result > operation:
            min_result = operation
        return
    else:
        f(i+1,operation+arr[i],op1-1,op2,op3,op4)
        f(i + 1, operation - arr[i], op1 , op2-1, op3, op4)
        f(i + 1, operation * arr[i], op1, op2, op3-1, op4)
        if operation<0:
            f(i + 1, -(abs(operation) // arr[i]), op1, op2, op3, op4-1)
        else:
            f(i + 1, operation // arr[i], op1, op2, op3, op4-1)



N = int(input())
arr = list(map(int, input().split()))
op1, op2, op3, op4 = list(map(int, input().split()))
min_result = 10e11
max_result = -10e11
# cnt = 0
f(1,arr[0],op1,op2,op3,op4)
print(max_result)
print(min_result)
# print(cnt)