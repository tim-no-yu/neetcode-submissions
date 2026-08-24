class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for n in nums:
            my_set.add(n)
        if len(nums) == len(my_set):
            return False
        return True