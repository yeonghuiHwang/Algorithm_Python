def solution(n):
    # sorted 사용
    return int(''.join(sorted(str(n), reverse=True)))
    
    