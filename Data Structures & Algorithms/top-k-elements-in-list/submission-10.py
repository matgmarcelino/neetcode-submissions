class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        idx = 0
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if idx == k:
                    return res
                res.append(num)
                idx += 1

        return res


        