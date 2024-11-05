import heapq

n = int(input()) # 후보의 수
votes = [int(input()) for _ in range(n)]

# 다솜이의 득표 수
dasom = votes[0]

# 다른 후보들의 득표 수를 최대 힙으로 관리
other_votes = [-v for v in votes[1:]] # 음수로 변환하여 최대 힙으로 사용
heapq.heapify(other_votes) # 힙의 특성을 지닌 리스트로 변환
# 기본적으로 최소 힙 지원
# index 0 -> 루트, 가장 작은 수
# 따라서 음수로 바꾸면 index 0에 가장 큰 수가 들어간다

cnt = 0 # 매수해야하는 사람 최소 수
while other_votes and (dasom <= -other_votes[0]):
    # otehr_votes(리스트가 비어있지 않고)
    # dasom 이가 가장 큰 득표수 보다 같거나 작을때
    max_votes = -heapq.heappop(other_votes)
    max_votes -= 1 # 상대 -1
    dasom += 1
    cnt += 1
    heapq.heappush(other_votes, -max_votes) # 줄어든 득표수를 다시 최대 힙에 넣음
    # 알아서 정렬
    
print(cnt)