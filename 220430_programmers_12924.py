"""
Finn은 요즘 수학공부에 빠져 있습니다. 
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15

자연수 n이 매개변수로 주어질 때, 
연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
"""

# 처음 풀이
# n 자신이 정답이 되는 경우를 생각하여 answer에 +1 ㄹ해줌
def solution(n):
    answer = 0
    a = 1
    sum = 0
    while a <= n // 2:
        for i in range(a, n + 1):
            sum += i
            if sum > n:
                a += 1
                sum = 0
                break
            elif sum == n:
                answer += 1
                sum = 0
                a += 1
                break
    
    return answer + 1

# 다른 풀이
# 효율성이 내가 푼 것보다 아주 조금 낮음
def solution(n):
    answer = 0
    for i in range(i, n + 1):
        sum = 0
        
        while i <= n:
            sum += i
            i += 1
            
            if sum == num:
                answer += 1
                break

    return answer

# 다른 풀이
# 자신보다 작은 홀수로 나누어떨이지는 값의 개수가 문제의 답.
# 즉, n의 약수 중 홀수인 것의 개수를 구하면 된다.
def solution(n):
    return len([i for i in range(1, num + 1, 2) if n % i == 0])
