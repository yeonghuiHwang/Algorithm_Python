def solution(phone_book): 

    # 1. hash_map을 생성
    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    
    # 2.접두어가 Hash map에 존재하는지 찾기 
    for nums in phone_book: 
        jda = "" 
        for num in nums:
          
            jda += num

            if jda in hash_map and jda != nums:       
                return False 

    return True