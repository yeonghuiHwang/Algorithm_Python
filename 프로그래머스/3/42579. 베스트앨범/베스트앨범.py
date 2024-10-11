def solution(genres, plays):
    answer = []

    dic1 = {}		# 장르별로 음악 담기 
    dic2 = {}		# 장르별 총 플레이 횟수를 저장

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]  # value를 list형태로 저장 (key값을 고정시키기 위해)
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p	# 플레이 횟수 더하기

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
  		# dic1의[k] 즉, 장르에있는 value 이므로 list를 가져오되, 정렬 기준은 뒤에 있는 재생횟수
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:	
            answer.append(i)

    return answer