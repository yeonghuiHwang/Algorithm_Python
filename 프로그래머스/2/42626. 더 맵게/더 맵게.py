# 우선순위 큐
import heapq

def solution(scoville, K):
    # 주어진 배열을 최소 힙으로 변환
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K : # 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
        if len(scoville) < 2 : # 더 섞을 수 없으면 -1 반환
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville) # 제일 작은 것 꺼내줌
        new_scoville = first + second * 2
        heapq.heappush(scoville, new_scoville) # 알아서 재정렬
        answer += 1 # 섞은 횟수 증가
    return answer