def solution(numbers):
    new_numbers = []
    answer = ''
    for num in numbers:
        new_numbers.append(str(num))
    new_numbers.sort(key=lambda x: x*3, reverse=True)
    answer=''.join(new_numbers)
    if answer[0] == '0':
        answer= '0'
    return answer