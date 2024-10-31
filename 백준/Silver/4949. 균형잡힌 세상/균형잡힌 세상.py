def is_balanced(string):
    stack = []
    for char in string:
        if char == '(' or char == '[':  # 여는 괄호를 스택에 추가
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':  # 스택이 비어있지 않고 마지막이 (이면 짝을 이룸
                stack.pop()
            else:
                return "no"
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return "no"
            
    return "yes" if not stack else "no"

while True:
    line = input()
    if line == ".":
        break
    print(is_balanced(line[:-1]))  # 문자열 끝의 "."을 제외하고 균형 검사
