"""
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
"""

# 처음 풀이
def solution(n):
    answer = sum(list(map(int, str(n))))

    return answer

# 리스트 컴프리헨션
def solution(n):
    answer = sum([int(i) for i in str(n)])

    return answer
