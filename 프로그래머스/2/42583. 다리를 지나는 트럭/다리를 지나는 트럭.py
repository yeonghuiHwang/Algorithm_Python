from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 1. 다리의 상태를 나타내는 큐 생성
    bridge = deque([0] * bridge_length) # 계속 이 크기 유지해야함
    truck_weights = deque(truck_weights) # 대기 중인 트럭들의 무게 리스트
    current_weight = 0 # 현재 다리 위의 트럭 총 무게
    time = 0 # 경과 시간
    
    # 2. 트럭들이 다리를 다 건널때까지 반복
    while truck_weights or current_weight > 0:
        # 한 번의 반복(= 1초 경과마다)
        time += 1
        
        # 2.1. 다리에서 가장 앞에 있는 트럭(혹은 빈 공간)을 내림
        exited_truck = bridge.popleft()
        current_weight -= exited_truck # 현재 무게에서 해당 트럭 무게를 뺌
        
        # 2.2. 다음 트럭이 다리에 오를 수 있는지 확인
        if truck_weights and current_weight + truck_weights[0] <= weight:
            # 다음 트럭을 다리에 추가할 수 있다면
            next_truck = truck_weights.popleft() # 대기열에서 트럭 꺼냄
            bridge.append(next_truck)
            current_weight += next_truck # 다리 위 무게 갱신
            
        else: 
            # 다음 트럭을 다리에 추가할 수 없다면
            bridge.append(0) # 빈 공간만 추가해 트럭 이동만 유지
            
    return time
            
        


'''
bridge_length = 2, weight = 10, truck_weights=[7,4,5,6]
시간 현재다리상태 다리위무게 대기트럭     설명
0   [0,0]       0     [7,4,5,6]  초기 상태(아직 다리에 트럭이 없음) 
1   [0,7]       7     [4,5,6]    트럭 7이 다리에 올라감, 다리 위 무게 7
2   [7,0]       7     [4,5,6]    트럭 7이 다리 위에서 한 칸 이동, 아직 다리 위에 있음
3   [0,4]       4     [5,6]      트럭 7이 다리를 건너고, 트럭 4가 다리에 오름
4   [4,5]       9     [6]        트럭 4가 다리 위에서 한 칸 이동, 트럭 5가 다리에 올라감
5   [5,0]       5     [6]        트럭 4가 다리를 건너고, 트럭 5가 다리 위에서 한 칸 이동
6   [0,6]       6     []         트럭 5가 다리를 건너고, 트럭 6이 다리에 올라감
7   [6,0]       6     []         트럭 6이 다리 위에서 한 칸 이동
8   [0,0]       0     []         트럭 6이 다리를 완전히 건넘(종료)
'''