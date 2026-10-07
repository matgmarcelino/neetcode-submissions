class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets: dict[str, List[str]] = defaultdict(list)

        for s in strs:
            key: str = "".join(sorted(s))
            buckets[key].append(s)

        return list(buckets.values())
    
