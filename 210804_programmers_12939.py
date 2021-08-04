"""
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
"""

# 처음 풀이
def solution(s):
    nums = s.split(' ')
    nums = list(map(int, nums))
    
    list1 = sorted([i for i in nums if i < 0])
    list2 = sorted([i for i in nums if i >= 0])
    
    list_ = list1 + list2
    
    return str(list_[0]) + ' ' + str(list_[-1])

# 정렬할 필요가 없었다...
def solution(s):
    nums = list(map(int, s.split(' ')))
    
    return str(min(nums)) + ' ' + str(max(nums))
