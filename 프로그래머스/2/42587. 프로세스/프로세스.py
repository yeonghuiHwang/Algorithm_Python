# 큐 -> FIFO
from collections import deque

def solution(priorities, location):
    queue = deque((p,i) for i,p in enumerate(priorities))
    # (우선 순위, 인덱스)
    # 인덱스 보존해야 나중에 큐에서 location이랑 비교 가능!
    # ex) queue -> [(2,0), (1,1), (3,2), (2,3)]
    
    order = 0 # 실행 순서
    
    while queue:
        # 큐가 빌때까지
        current = queue.popleft()
        
        # 참고 : any() : 조건이 하나라도 참이면 true, 모든 조건이 false면 false 반환
        # if any(currnet[0] < p[0] for p in queue)
        # 여기서는 포문으로 씀
        for p in queue:
            if current[0] < p[0]:
                # 하나라도 발견하면 더 조사할 이유가 없음 종료
                queue.append(current)
                break
        else:
            # 실행
            order += 1 # 실행 순서 
            if current[1] == location:
                return order
                

'''   
2,1,3,2
A B C D

1 3 2 2
B C D A

3 2 2 1
C D A B

pop

2 2 1
D A B

pop

2 1 
A B

pop

1
B

pop

스택 비면 종료
'''