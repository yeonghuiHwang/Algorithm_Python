# 문자열은 불변이다!!! 따라서 새로운 문자열을 생성해야함.

def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]
        