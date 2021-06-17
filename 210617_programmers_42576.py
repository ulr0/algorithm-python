"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
"""

# 처음 풀이 정확성 통과, 효율성 실패
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    answer = participant[0]
    return answer

# 정렬한 후 비교
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]

# hash 사용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

# collections 모듈 사용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
