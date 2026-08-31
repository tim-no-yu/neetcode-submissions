class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        rv = []
        count = 0
        ls = list(dic.items())
        # print(ls)
        while (count < k):
            # print(ls)
            max_key, max = ls[0][0], ls[0][1]
            # print(max_key, max)
            for i in range(len(ls)):
                key, v = ls[i][0], ls[i][1]
                if v > max:
                    max_key = key
                    max = v
            ls.remove((max_key, max))
            # print(ls)
            rv.append(max_key)
            count += 1
        return rv
