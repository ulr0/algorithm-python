"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Since an empty string reads the same forward and backward, it is a palindrome.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# 처음 풀이
# 51 ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is False:
            return True
        
        string = "".join(char.lower() for char in s if char.isalnum())
        if string == string[::-1]:
            return True
        else:
            return False

# 리스트를 이용한 풀이
# 250 ms
# 리스트.pop(index) 는 O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        listed_string = [char.lower() for char in s if char.isalnum()]
        
        for char in s:
            if char.isalnum():
                listed_string.append(char.lower())

        while len(listed_string) > 1:
            if listed_string.pop(0) != listed_string.pop():
                return False

        return True

# 데크를 이용한 풀이
# 87 ms
# 데크.popleft() = O(1)
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = deque()

        for char in s:
            if char.isalnum():
                d.append(char.lower())

        while len(d) > 1:
            if d.popleft() != d.pop():
                return False

        return True

# 정규식 + 슬라이싱
# 53 ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()

        string = re.sub("[^a-z0-9]", "", string)

        return string == string[::-1]
