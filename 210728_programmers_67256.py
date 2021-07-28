"""
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
"""

# 처음 풀이
def solution(numbers, hand):
    answer = ''
    distance = {2:{1:1, 2:0, 3:1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3, 0:3, -1:4},
               5:{1:2, 2:1, 3:2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2, 0:2, -1:3},
               8:{1:3, 2:2, 3:3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1, 0:1, -1:2},
               0:{1:4, 2:3, 3:4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2, 0:0, -1:1}}
    left = -1
    right = -1
    for i in numbers:
        if i in (1, 4, 7):
            answer += 'L'
            left = i
        if i in (3, 6, 9):
            answer += 'R'
            right = i
        if i in (2, 5, 8, 0):
            if distance[i][left] > distance[i][right]:
                answer += 'R'
                right = i
            if distance[i][left] < distance[i][right]:
                answer += 'L'
                left = i
            if distance[i][left] == distance[i][right]:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
    return answer

# 키패드를 좌표로 나타냄
def solution(numbers, hand):
    answer = ''
    
    location = {1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
            4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
            7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
            '*' : (3, 0), 0 : (3, 1), '#' : (3, 2)}
    
    left = '*'
    right = '#'
    
    for i in numbers:
        if i in (1, 4, 7):
            answer += 'L'
            left = i
        elif i in (3, 6, 9):
            answer += 'R'
            right = i
        else:
            left_distance = abs(location[i][0] - location[left][0])\
                        + abs(location[i][1] - location[left][1])
            right_distance = abs(location[i][0] - location[right][0])\
                         + abs(location[i][1] - location[right][1])
            if left_distance > right_distance:
                answer += 'R'
                right = i
            elif left_distance < right_distance:
                answer += 'L'
                left = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
    return answer
