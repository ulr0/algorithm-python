"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.
"""

# a, b 의 최소공배수lcm = (a * b) // 최대공약수 gcd(a, b)
# math 라이브러리에 gcd 함수 사용 가능
# lcm 함수도 있으나 파이썬 3.9+ 사용 가능

from math import gcd
def solution(arr):
    answer = 1

    for i in arr:
        answer = (answer * i) // gcd(answer, i)

    return answer

# gcd 구하는 함수 만들기
# a, b의 gcd = b, a%b의 gcd 
# b가 0이 될 때 a가 최대공약수가 된다.
def gcd(a, b):
    if b == 0:
        return a
    else:
        a, b = b, a % b
    return gcd(a, b)

#즉
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
