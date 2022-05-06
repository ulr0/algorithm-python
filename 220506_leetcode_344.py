"""
Write a function that reverses a string. 
The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

# 처음 풀이
# 195 ms
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# 스왑
# 208 ms
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

# 슬라이싱
# 198 ms
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
