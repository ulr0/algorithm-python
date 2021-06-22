"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

# itertools import해서 사용
from itertools import combinations

def solution(nums):
    answer = 0
    coms = [sum(i) for i in combinations(nums, 3)]
    
    for i in coms:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer += 1
                
    return answer
