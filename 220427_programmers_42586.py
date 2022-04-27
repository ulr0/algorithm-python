"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이 때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
"""

# 나의 풀이
def solution(progresses, speeds):
    answer = []
    
    left_days = []
    for p, s in zip(progresses, speeds):
        days = (100 - p) // s
        if (100 - p) % s != 0:
            days += 1
        left_days.append(days)

    a = left_days[0]
    count = 0
    for i in range(0, len(left_days)):
        if left_days[i] <= a:
            count += 1
            if i == len(left_days) - 1:
                answer.append(count)
        else:
            answer.append(count)
            count = 1
            a = left_days[i]
            if i == len(left_days) - 1:
                answer.append(count)
                
    return answer

"""
배포까지 남은 날짜를 구하는 부분을 if문 없이 구하려면
(p-100)//s 로 계산해서 음수로 몫을 구하고
-((p-100)//s) 다시 양수로 바꿔주면 된다.

-7 // 2 를 연산하면 -3이 아닌 -4인 것을 이용.
"""

# 수정
def solution(progresses, speeds):
    answer = []
    left_days = [-((p-100)//s) for p, s in zip(progresses, speeds)]

    a = left_days[0]
    count = 0
    for i in range(0, len(left_days)):
        if left_days[i] <= a:
            count += 1
            if i == len(left_days) - 1:
                answer.append(count)
        else:
            answer.append(count)
            count = 1
            a = left_days[i]
            if i == len(left_days) - 1:
                answer.append(count)
                
    return answer
