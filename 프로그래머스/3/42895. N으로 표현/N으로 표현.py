def solution(N, number):
    
    """
    4번 사칙 연산 한 것은
    - (1번 사칙연산 한 것)과 (3번 사칙연산 한 것)의 사칙연산이다. 마찬가지로,
    - (2번 '')과 (2번 '')의 사칙연산
    - (3번 '')과 (1번 '')의 사칙연산이다.
    
    사칙연산을 몇번하는지 누적돼어 집합끼리 합할떄 ..
    i번째와 i-j번째
    5     5-3
    """
    
    # 빈 집합 정의 9개까지 정의 - 최솟값이 8보다 크면 -1을 리턴하므로 8개 55...55면 된다.
    sets = [set() for _ in range(9)]
    
    # N, NN, NNN, .. 조합 미리 만들어주기
    for i in range(1,9):
        sets[i].add(int(str(N)*i))
        
    # dp 동적계획법 (N을 i개 사용하여 만들 수 있는 수 구하기)
    for i in range(1,9):
        for j in range(1,i):
            
            for op1 in sets[j]:
                for op2 in sets[i-j]:
                    sets[i].add(op1+op2)
                    sets[i].add(op1-op2)
                    sets[i].add(op1*op2)
                    
                    if op2 != 0:
                        sets[i].add(op1//op2)
        if number in sets[i]:
            return i
    
    return -1
