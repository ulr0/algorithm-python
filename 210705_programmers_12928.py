"""
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
"""

# 처음 풀이
def solution(n):
    divisor = []
    for i in range(1, int(n**0.5+1)):
        if n % i == 0:
            print(i)
            divisor.append(i)
            divisor.append(n // i)
    return sum(set(divisor))
