from collections import deque
import sys
input = sys.stdin.readline

def queue_card():
    n = int(input().strip()) 
    queue = deque()
    
    for i in range(n):
        queue.append(i + 1)  # 1부터 n까지 숫자를 큐에 추가
    
    while True:
        if len(queue) == 1: 
            break  # 카드가 한 장 남으면 반복 종료
        else:
            queue.popleft()  # 맨 위의 카드 버림
            if len(queue) == 1: 
                break  # 카드가 한 장 남으면 반복 종료
            queue.append(queue.popleft())  # 두 번째 카드를 맨 뒤로 이동
            
    print(queue[0])  # 마지막 남은 카드 출력

queue_card()
