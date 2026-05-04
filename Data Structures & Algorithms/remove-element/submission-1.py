class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            while val in nums:
                for num in nums:
                    if num == val:
                        nums.remove(num)
            return len(nums)