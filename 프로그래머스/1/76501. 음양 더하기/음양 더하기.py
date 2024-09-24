def solution(absolutes, signs):
    # 절댓값 차례대로
    # 실제 부호 boolean 차례대로
    total = 0
    for i in range(len(signs)):
        if signs[i]:
            total += absolutes[i]
        else:
            total -= absolutes[i]
    
    return total