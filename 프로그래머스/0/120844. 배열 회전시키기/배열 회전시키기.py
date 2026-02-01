def solution(numbers, direction):
    new_list = []
    
    # 문자열과 리스트는 더할 수 없다. 리스트 + 리스트만 더할 수 있따.
    if direction == "right":
        new_list = [numbers[-1]] + numbers[:-1]
    elif direction == "left":
        new_list = numbers[1:] + [numbers[0]]
    return new_list