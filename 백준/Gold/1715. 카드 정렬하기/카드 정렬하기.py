from queue import PriorityQueue

pq = PriorityQueue()

n = int(input())
p = [0] * n

for i in range(n):
    p[i] = int(input())
   
# 최소 힙 
for i in range(n):
    pq.put(p[i])

cnt = 0
sum = 0

if n == 1:
    print(cnt)
else: # 두개부터면
    while True:
    # 가장 작은 두 수 꺼냄
        a = pq.get()
        b = pq.get()
        cnt = a + b
        sum += cnt
        if (pq.qsize() == 0):
            break
        pq.put(a+b) # 합을 삽입!
    print(sum)