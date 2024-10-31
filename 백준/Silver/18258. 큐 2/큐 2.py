# 정수 구현하는 큐(FIFO)
# push X 
# pop(큐에서 가장 앞에 있는 정수 빼고 출력(가장 먼저 들어온), 비어있으면 -1
# size (큐 정수 개수)
# empty 큐가 비어있어면 1, 아니면 0
# front 큐의 가장 앞에 있는 정수 출력, 없으면 -1
# back 큐의 가장 뒤에 있는 정수 출력, 없으며 -1
# 큐 : back은 삽입, front는 삭제만

from collections import deque
import sys
input = sys.stdin.readline

def process_queue_commands():
    queue = deque() # 빈 deque 생성해서 큐로 사용
    n = int(input().strip()) # 첫 번째 줄에서 명령어의 수 입력 받음
    result = [] # 출력할 결과를 저장할 리스트
    
    for _ in range(n): # n번 반복해서 각 명령 처리
        command = input().strip().split() # 명령어를 입력받고 공백을 제거하고 리스트로 만듬
        
        # push X
        if command[0] == 'push':
            queue.append(int(command[1])) # 두 번째 요소 command[1] 정수로 변환하여 추가
        # pop X : FIFO
        elif command[0] == 'pop':
            if queue: 
                result.append(queue.popleft())
            else:
                result.append(-1) # 비어있으면 -1 출력해야함
        # size
        elif command[0] == 'size':
            result.append(len(queue))
        
        # empty
        elif command[0] == 'empty':
            result.append(1 if not queue else 0)
        
        # front (가장 먼저 들어온 애)
        elif command[0] == 'front':
            if queue:
                result.append(queue[0])
            else:
                result.append(-1)
        # back (가장 마지막에 들어온 애)
        elif command[0] == 'back':
            if queue:
                result.append(queue[-1])
            else:
                result.append(-1)
        
    # 모든 명령 처리 후, 결과 리스트 한 번에 출력
    print("\n".join(map(str, result))) # map()으로 숫자를 문자열로 바꾼 다음 줄바꿈으로 합침
    
process_queue_commands()