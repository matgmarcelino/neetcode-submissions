class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter: dict[int, int] = defaultdict(lambda: 0)

        for num in nums:
            counter[num] += 1

        # index: frequency | value: num
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        res: List[int] = [0] * k
        idx: int = 0

        for i in range(len(buckets) - 1, 0, -1):
            if not buckets[i]: continue

            for num in buckets[i]:
                res[idx] = num
                idx += 1

                if (idx == k):
                    return res
               

        

