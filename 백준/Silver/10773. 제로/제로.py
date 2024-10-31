def calculate_sum():
    k = int(input())  # 정수의 개수 입력
    stack = []  # 스택 초기화
    
    for i in range(k):
        num = int(input())
        if num == 0:  # 잘못된 수를 입력받으면 가장 최근의 값을 스택에서 제거
            if stack:  # 스택이 비어있지 않을 때만 pop 수행
                stack.pop()
        else:
            stack.append(num)  # 정수를 스택에 추가

    return sum(stack)  # 스택의 모든 수의 합을 반환

result = calculate_sum()
print(result)
