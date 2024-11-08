# SJF(Shortest Job First) algorithm 
# 가능한 작업들 중에서 소요 시간이 가장 짧은 작업을 먼저 처리, 평균 대기 시간(대기한 시간 + 실행된 시간 다 더해서 작업 수로 나눔) 최소화 가능

# 현재 시간에 이미 도착한 작업들만을 고려, 따라서 현재 가능 작업 중 소요 시간이 가장 짧은 것을 선택하는게 최선의 선택!

import heapq as hq

# 걸린 시간을 가장 줄여야함
def solution(jobs):
    # jobs -> [작업이 요청되는 시점, 작업의 소요 시간]
    # sort -> 디폴트는 작업이 요청되는 시점 순으로
    # jobs.sort(key=lambda x: x[1]) 다른 기준으로 정렬 설정 가능
    jobs.sort() # 요청 시점이 가장 빠른 순서대로 정렬 -> 그 다음에는 소요 시간이 제일 작은 것 기준으로 해야함
    heap = [] # 최소 힙 사용해 현재 가능 작업 중 가장 짧은 소요 시간의 작업 선택
    time = 0 # 현재까지 진행된 시간
    total_time = 0
    index = 0
    cnt = 0
    
    # 모든 작업 처리될 때까지 반복
    while cnt < len(jobs):
        # 현재 시간까지 도착한 모든 작업 힙에 넣기
        while index < len(jobs) and jobs[index][0] <= time: # 도착해서 대기 중이면 소요 시간 비교해서 넣기!
            hq.heappush(heap, (jobs[index][1], jobs[index][0])) # (소요 시간, 요청 시간) 형태로 힙에 추가 -> 소요 시간 작은 순서로 정렬
            index += 1
            
        if heap:
            # 가장 짧은 소요시간 걸리는 작업 꺼내어 처리
            duration, start_time = hq.heappop(heap)
            time += duration # 현재 시간 갱신
            total_time += time - start_time
            cnt += 1
        
        else:   
            # 현재 시점까지 도착한 작업이 없다면 다음 작업 요청 시간 이동
            # jobs = [[0, 3], [5, 2], [6, 1]] 예제처럼 time = 3인데 다음 작업 5,2는 요청 시간이 5이므로 아직 도착 안함
            # 이때 else 실행해서 5로 이동
            time = jobs[index][0]
            
    return total_time // len(jobs)
    

# 각 작업의 종료 시점 저장 필요
# jobs = jobs = [[0, 3], [5, 2], [6, 1]]
