def solution(x):
    result = sum(int(i) for i in str(x))
    if x%result == 0:
        return True
    else:
        return False