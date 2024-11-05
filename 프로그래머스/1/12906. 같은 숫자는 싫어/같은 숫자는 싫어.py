def solution(arr):

    answer = []
    
    for num in arr:
        # 배열이 비어있거나, 마지막 원소와 다른 경우 추가
        if not answer or answer[-1] != num: # 비어있으면 -1 확인을 할 수가 없음
            answer.append(num)
            
    return answer