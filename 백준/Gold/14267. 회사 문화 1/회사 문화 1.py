# 상사가 부하 칭찬 -> 그 부하의 부하들 전부 칭찬
# 노드 -> 자식 노드 -> 자식 노드 ... 전부 칭찬
# 칭찬 수치 동일

n,m = map(int, input().split())
parent = list(map(int, input().split()))

for i in range(1,n):
    parent[i] -= 1 # 노드 번호가 문제에서는 1부터 시작하므로 편하게 -1 한 후 시작한다 !
    # 0번 인덱스는 루트, 따라서 항상 -1이어야함 주의

good = [0] * n
for _ in range(m):
    id, score = map(int,input().split())
    # 칭찬 배열(누적이 아니라, 총 받은 칭찬 수치, 부모로부터 받은 칭찬까지 누적된 배열이 아님)
    good[id-1] += score
    
total_good = [0] * n
for i in range(1, n):
    total_good[i] += total_good[parent[i]] + good[i]
    
print(*total_good)
# * : 언패킹 연산자 사용, 리스트나 튜플 등의 모든 요소 개별로 꺼내주므 공백을 기준으로 출력해줌