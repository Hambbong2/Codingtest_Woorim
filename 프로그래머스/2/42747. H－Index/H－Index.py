def solution(citations):
    citations.sort(reverse=True) # 좀 외워라
    
    for idx in range(len(citations)):
        
        if citations[idx] < idx+1:
            return idx
    
    return len(citations)


"""
다른 풀이: 이분탐색
def solution(citations):
    citations.sort()
    n = len(citations)
    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2
        count = sum(c >= mid for c in citations)
        
        if count >= mid:
            left = mid + 1
        else:
            right = mid - 1
    return right



"""


"""
이 문제..
* 인덱스 0번부터 시작
* “값”이랑 “개수”를 동시에 다룸
* “처음 실패한 순간”을 이용하는 로직

1. avail_hindex 인덱스에 최대값이라 판단된 수
    2. avail_hindex 보다 작으면 애초에 검사할 필요 없음
    3. avail_hindex를 찾기 위해 검사
        1. 
        [0,1,3,5,6] 전체 길이(5) - 현재인데스(2) = 3 인용횟수 3
        [0,0,0,0,1] 전체 길이(5) - 현재 인데스(4) = 1 조금 안맞기는한데 1개는 인용횟수가 있는거
        [1,1,2,4,5] 없음
        
    오름차순보다 내림차순으로 할까? - 시간복잡도 sort reverse해서 n^2
    (변경) 'h편 이상'
    [6,5,3,1,0] 타켓 수 = 인덱스 + 1
                3     = 2 + 1
    [1,0,0,0,0] 1     = 0 + 1
    [5,4,4,3,1] 3    <= 3  -> 굳이 2안해도 되고 종료 가능..
               5 <= 0 + 1
               4 <= 1 + 1
               4 <= 2 + 1 - 사실 3이어야 하는데 갱신되도록해야함. 근데 어차피 조건에 안맞아서 넘어가
               3 <= 3 + 1
    """