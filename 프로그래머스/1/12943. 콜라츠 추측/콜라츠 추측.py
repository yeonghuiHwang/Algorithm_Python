def solution(num):
    if num==1:
        return 0
    
    cnt = 0
    while num!=1:
        # 1이 될때까지 반복하다가
        # 500번 넘으면 -1 반환
        if cnt>=500:
            return -1
        if num%2==0:
            # 짝수일때
            num//=2
        else:
            num = num*3 + 1
        
        cnt+=1
    return cnt
            
    