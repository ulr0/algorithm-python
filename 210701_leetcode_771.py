"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
# 처음 풀이 32ms
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for i in range(len(jewels)):
            answer += stones.count(jewels[i])
        return answer

# 두 번째
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for i in stones:
            if i in jewels:
                answer += 1
        return answer
