"""
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
"""

# 처음 풀이
def solution(n):
    answer = []
    reverse = str(n)[::-1]
    for i in reverse:
        answer.append(int(i))
        
    return answer

# map 사용
def solution(n):
    reverse = reversed(str(n))
    answer = list(map(int, reverse))
