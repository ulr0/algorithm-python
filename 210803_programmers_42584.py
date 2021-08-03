"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

입출력 예
prices	        return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
"""

# 처음 풀이
def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
            if j == len(prices) - 1:
                answer.append(j-i)
    answer.append(0)
        
    return answer

# 다른 풀이
def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
        
    return answer


