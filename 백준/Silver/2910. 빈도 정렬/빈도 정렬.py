"""
1. 람다식 사용
- 일반적인 람다식과 sort 할 때의 key값에 들어가는 람다식은 다르다.
- 람다식은 이때 우선순위 정렬 역할을 한다.
- 애초에 람다식 표현식이 얼설픈 것 같다. 정확히 알아두자,

2. sort()는 리스트만 가능하다. 딕셔너리와 같은건 sorted만 가능하다.

3. key는 람다식이나 함수만 가능하다.



"""

N, C = map(int, input().split())

index_dict = {}
cnt_dict = {}
res = []

original_list = list(map(int, input().split()))

# 빈도
for idx in range(len(original_list)):
    
    if cnt_dict.get(original_list[idx],0) != 0:
        cnt_dict[original_list[idx]] += 1
    else:
        cnt_dict[original_list[idx]] = 1
        index_dict[original_list[idx]]= idx

# cnt_dict.sort(key = cnt_dict.values()) # sort는 리스트 전용. # 그리고 key에 들어갈 것은 '함수'나 '람다식'이어야함. 리스트는 x

# sorted(반복가능한객체, key=정렬기준함수, reverse=True/Fasle)
sorted_keys = sorted(cnt_dict.keys(), key = lambda x : (-cnt_dict[x], index_dict[x]))

# 출력
for k in sorted_keys:
    
    for _ in range(cnt_dict[k]):
        res.append(k)

print(*res)