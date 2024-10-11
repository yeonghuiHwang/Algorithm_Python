def solution(nums):
    kind = set()
    kind.add(nums[0])
    limit = len(nums) * 0.5
    
    for pkm in nums:
        if(len(kind) == limit):
            break
        kind.add(pkm)
    
    answer = len(kind)
    return answer
