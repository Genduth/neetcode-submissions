class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        while len(ans) != 2* len(nums):
            for num in nums:
                ans.append(num)
        return ans