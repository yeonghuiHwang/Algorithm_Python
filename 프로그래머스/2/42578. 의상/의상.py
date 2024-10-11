def solution(clothes):
    hash_map = {}
    
    for clothe, type in clothes:
         # type이란 키가 없으면 default값으로 0을 value로 주겠다.
        hash_map[type] = hash_map.get(type, 0) + 1 
    
    answer = 1
    # dict로 for문 돌리면 키값으로 순회한다
    for type in hash_map:
        answer *= (hash_map[type] + 1)
    
    return answer - 1