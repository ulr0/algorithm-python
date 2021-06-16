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
