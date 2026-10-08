class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
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


        