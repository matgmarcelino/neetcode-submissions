class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        common = Counter(nums).most_common(k);
        
        buckets = []
        for el in common:
            buckets.append(el[0])

        return buckets
        
