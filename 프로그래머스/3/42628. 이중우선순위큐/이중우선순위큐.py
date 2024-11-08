import heapq

def solution(operations):
    min_heap, max_heap = [], []
    visited = [False] * 1000000  # 각 값의 유효성 체크를 위한 리스트
    # 값이 삭제되면 False 부여하여 유효하지 않음을 표시
    index = 0

    for operation in operations:
        op, value = operation.split()
        value = int(value)

        if op == 'I':
            heapq.heappush(min_heap, (value, index))
            heapq.heappush(max_heap, (-value, index))
            visited[index] = True
            index += 1
            
        elif op == 'D' and value == 1:
            # 최댓값 삭제
            while max_heap and not visited[max_heap[0][1]]:
                # 유효하지 않은 값들 삭제
                heapq.heappop(max_heap)
            if max_heap:
                # 유효한 최댓값 제거
                _, idx = heapq.heappop(max_heap) # -value, index
                visited[idx] = False
        elif op == 'D' and value == -1:
            # 최솟값 삭제
            while min_heap and not visited[min_heap[0][1]]:
                # 유효하지 않은 값들 삭제
                heapq.heappop(min_heap) 
            if min_heap:
                # 유효한 최솟값 제거
                _, idx = heapq.heappop(min_heap) # value, index
                visited[idx] = False

    # 유효하지 않은 값 제거, 최종 값 보장
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    return [-max_heap[0][0], min_heap[0][0]]

# 예제 입력 확인
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))  # 출력: [0, 0]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))  # 출력: [333, -45]
