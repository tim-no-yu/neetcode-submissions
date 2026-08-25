class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use hashmap
        dic = {}
        #add values
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dic:
                return [dic[diff], i]
            else:
                dic[v] = i