class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rv = defaultdict(list)
        for string in strs:
            nums = [0] * 26
            for c in string:
                nums[ord(c) - ord('a')] += 1
            rv[tuple(nums)].append(string)
        return list(rv.values())