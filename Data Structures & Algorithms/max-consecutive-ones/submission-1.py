class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        stage = []
        for num in nums:
            if num == 1:
                stage.append(1)
                if longest < len(stage):
                    longest = len(stage)
            elif num == 0:
                stage = []
        return longest   