def solution(n):
    
    list = []
    while n > 0:
        list.append(n%10)
        n//=10
        
    return sum(list)
        

    