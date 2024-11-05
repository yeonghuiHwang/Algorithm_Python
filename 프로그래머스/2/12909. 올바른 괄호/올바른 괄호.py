def solution(s):
    stack = []
    for char in s:
        # 여는 괄호 추가
        if char == '(':
            stack.append(char)
        elif not stack : return False
        elif stack and char == ')':
            # 스택이 비어있지 않고, 마지막 괄호면 짝을 이룸
            stack.pop()
            
    return True if not stack else False