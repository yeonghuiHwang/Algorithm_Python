# task
'''
1. 남은 일수 계산, (100-progresses) / speeds 올림 계산
2. 배포 그룹 결정 
-> 첫 번째 작업 완료 기준으로
'''
import math

def solution(progresses, speeds):
    # 남은 일수 계산
    days = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    
    answer = []
    current_max = days[0]
    cnt = 1
    
    # 배포 그룹 계산
    for day in days[1:]:
        if day <= current_max:
            # 현재 기준일보다 빨리 끝남, 같은 배포 그룹에 설정
            cnt += 1
        else:
            # 현재 기준일보다 늦게 끝나면, 다른 배포 그룹에 설정
            answer.append(cnt)
            current_max = day
            cnt = 1
    
    # 마지막 배포 그룹 추가
    answer.append(cnt)
    
    return answer