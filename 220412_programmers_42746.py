"""
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이 중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
"""

# 첫 번째 풀이
"""
삽입 정렬
두 숫자를 문자로 바꾸고 더해서 비교연산을 하는 to_swap 함수를 만든다.
True를 반환하면 두 숫자의 위치를 변경하는 것을 반복.
시간복잡도 O(n^2)
"""
def to_swap(n1, n2):

    return str(n1) + str(n2) > str(n2) + str(n1)


def solution(numbers):
    i = 1
    while i < len(numbers):
        j = i
        while j > 0: 
            if to_swap(numbers[j], numbers[j-1]):
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
                j -= 1
            else:
                break
        i += 1

    return str(int(''.join(map(str, numbers))))

# 다른 풀이
"""
리스트를 문자열로 바꿔서 정렬할 경우 '30'과 '3' 중 '30'이 더 큰 수이지만
가장 큰 수를 만들기 위해서는 ['30', '3']이 아닌 ['3', '30'] 순으로 정렬되어야 한다.
'3n'의 일의자리 숫자가 '3'보다 작을 경우 '3'이 '3n'보다 우선순위가 되어야 한다는 것.
각 자리마다 크기를 비교하기 위해서
제한사항에서 모든 원소는 0 이상 1,000 이하인 것을 이용한다.
가장 적은 한자리 수를 세 자리 수로 바꾸어 모든 자리의 숫자 크기를 비교할 수 있게
모든 원소를 문자열로 바꾼 후 *3 해준 후 정렬한다.
"""

def solution(numbers): 
    if sum(numbers) == 0:
        return '0'
    
    strings = list(map(str, numbers))
    sorted_strings = sorted(strings, key=lambda x: x*3, reverse=True) 
    
    return ''.join(sorted_strings)
