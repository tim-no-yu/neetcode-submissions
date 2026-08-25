class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1): #len = 4, 4-1=3, 0-2
            for j in range(i + 1, len(nums)): #2, 1-2
                if (nums[i] + nums[j]) == target:
                    return [i, j]