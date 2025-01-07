def solution(a, b, n):
    answer = 0
    while n>=a:
        for bottle in range(n,0,-1):
            if bottle%a==0:
                break
        back=(bottle//a)*b
        answer+=back
        n=n-bottle+back
        
    return answer