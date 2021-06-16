"""
어떤 정수들이 있습니다. 
이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 
이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
"""

# 처음 풀이
def solution(absolutes, signs):
    list = []
    for pair in zip(absolutes, signs):
        if pair[1] is False:
            list.append(-pair[0])
        else:
            list.append(pair[0])
    
    answer = 0
    for i in list:
        answer += i
    
    return answer

# 수정
def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        if j is True:
            answer += i
        else:
            answer -= i
    
    return answer
