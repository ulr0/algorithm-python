"""
2016년 1월 1일은 금요일입니다. 
2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다. 
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
"""

# 처음 풀이
from datetime import datetime

def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    a = datetime(2016, a, b)
    b = datetime(2016, 1, 1)
    c = (a - b).days % 7
    answer = days[c]
    
    return answer

# 모듈 사용하지 않고 풀기
def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    a = (sum(months[:a-1]) + b - 1) % 7
    answer = days[a]
    
    return answer
