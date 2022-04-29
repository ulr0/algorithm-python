"""
Leo는 카펫을 사러 갔다가 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
"""

# 처음 풀이
# 중앙의 yellow의 가로와 세로인 x, y를 구해서 전체의 가로, 세로 구함.
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    y = int(yellow ** 0.5)
    while True:
        if yellow % y != 0:
            y -= 1
            continue
            
        if (y + 2) * ((yellow // y) + 2) != total:
            y -= 1
            continue
        
        x = yellow / y
        answer.append(x + 2)
        answer.append(y + 2)
        break
    return answer

# 다른 풀이
# yellow의 (가로 + 세로) * 2 는 brown의 개수(카펫 둘레) - 4(모서리)인 것을 이용한다.
def solution(brown, yellow):
    for height in range(1, int(yellow ** 0.5) + 1):
        if yellow % height == 0:
            width = yellow // height
            if (width + height) * 2 == brown - 4:
                return [width + 2, height + 2]
