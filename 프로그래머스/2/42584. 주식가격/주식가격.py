def solution(prices):
    stack = [] # 가격이 떨어지지 않은 시간에 대한 정보를 담을 스택(index 저장)
    answer = [0] * len(prices)
    # 스택의 마지막 인덱스는 가장 최근에 가격이 떨어지지 않은 시점
    for i in range(len(prices)):
        while stack and prices[i]<prices[stack[-1]]: # 스택이 비어있지 않고 현재 가격이 스택의 마지막 인덱스에 있는 가격보다 낮으면, 가격이 떨어졌다는 의미
            j = stack.pop() # 떨어진 가격의 인덱스를 스택에서 꺼냄 본 예시에서 맨 처음 꺼내지는 인덱스 상황 i =3, j=2
            answer[j] = i-j # 현재 시점에서 떨어진 시점까지의 시간 계산
        stack.append(i) # 현재 인덱스 스택에 추가
    # 끝나고나면 stack = [0,1,3,4]
    
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    
    return answer