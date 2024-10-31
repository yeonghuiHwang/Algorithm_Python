import sys
input = sys.stdin.readline

def last_card(n):
    power = 1
    # power 변수를 사용하여 주어진 숫자 n에 가장 가까운 (또는 작거나 같은) 2의 거듭 제곱을 찾기 위해 작성한 것
    while power * 2 <= n:
        power *= 2
    if power == n:
        return n
    else:
        return (n - power) * 2

# 입력 및 출력
n = int(input().strip())
print(last_card(n))