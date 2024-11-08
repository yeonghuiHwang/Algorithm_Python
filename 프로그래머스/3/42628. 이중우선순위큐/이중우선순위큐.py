import heapq as hq

def solution(operations):
    min_heap, max_heap = [],[]
    
    for op in operations:
        op, value = op.split() # 문자열을 공백으로 분리
        value = int(value)
        
        if op == 'I':
            hq.heappush(min_heap, value)
            hq.heappush(max_heap, -value)
        # 최댓값 삭제
        elif op == 'D' and value == 1:
            if max_heap :
                max_value = -hq.heappop(max_heap) # 알아서 정렬
                min_heap.remove(max_value) # 알아서 정렬해주지 않음
                hq.heapify(min_heap)
        elif op == 'D' and value == -1:
            if min_heap :
                min_value = hq.heappop(min_heap)
                max_heap.remove(-min_value)
                hq.heapify(max_heap)
                
    if not min_heap: 
        return [0,0]
    return [-hq.heappop(max_heap), hq.heappop(min_heap)]