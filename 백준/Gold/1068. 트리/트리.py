n = int(input()) # node의 개수
parent = list(map(int, input().split())) # 공백 제거, 받은 문자열을 정수형으로 바꾸고 리스트로 만드는 과정
r = int(input()) # 삭제할 노드의 인덱스

# 예시 그림에서는 루트 노드 번호가 0 그러나 실제로는 0이 아닐 수도 있기 때문에 루트 노드를 우선 찾아야 함
# 루트 노드 찾기
for i in range(n):
    if parent[i] == -1:
        root = i # 루트 노드의 부모 없으므로 parent 배열 값이 -1
        break
    
# 사라지는 노드를 판별(검은색으로 칠하자!)
black = [0] * n # 색칠이 하나도 되어있지 않은 길이 n짜리 배열을 선언
for i in range(n):
    # 각 노드마다 계속 부모 노드로 올라가면서 만약 r번 노드를 마주친다면 사라지는 노드임이 판별 가능! 검은색으로 칠하기!
    # i 번째 노드가 사라질 노드인가?
    u = i
    while True:
        if u == r:
            black[i] = 1
            break
        if u == root:
            # 계속 올라가다가 r을 만나지 않고 루트 노드랑 만난다면 i는 지워지지 않는 노드
            break
        u = parent[u] # 갱신
        
# 자식이 있는 노드들 빨간색으로 칠하기. 루트부터 내려가서 선택한 노드가 부모가 존재한다면 그 부모노드를 색칠하면됨 (parent 배열 이용)
red = [0] * n
for i in range(n):
    if black[i] == 1:
        # 만약 검정색 노드(즉 지워지는 노드이면 -> 지워지는 노드는 고려할 필요가 없으니 그냥 넘어감)
        continue
    # 검정색 노드가 아니면 부모에 색칠!
    if i == root:
        # 루트이면 그냥 넘어감
        continue
    red[parent[i]] = 1
    
    
cnt = 0
for i in range(n):
    if black[i] == 1 or red[i] == 1:
        continue
    else: cnt+=1
    
print(cnt)