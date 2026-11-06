class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = defaultdict(int)

        for num in nums:
            count[num] += 1

        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res: List[int] = []
        for i in range(len(buckets) - 1, 0, -1):
            for bucket in buckets[i]:
                res.append(bucket)
                if len(res) == k:
                    return res