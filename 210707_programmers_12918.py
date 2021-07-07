"""
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
"""

# 처음 풀이
def solution(s):
    answer = False
    string = 'abcdefghijklmnopqrstuvwxyz'
    if len(s) == 4 or len(s) == 6:
        answer = True
    for i in s:
        if i in string: 
            answer = False

    return answer

# try except
def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6
