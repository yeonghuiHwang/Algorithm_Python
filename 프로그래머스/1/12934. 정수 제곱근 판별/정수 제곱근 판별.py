def solution(n):
    for i in range(1, n+1):
        if i*i == n:
            return (i+1)*(i+1)
    return -1
# n으로 루프 설정하지 않도록 주의해