class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        buckets = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            bucket = buckets.get(sorted_s, [])
            bucket.append(s)
            buckets[sorted_s] = bucket

        for val in buckets.values():
            res.append(val)

        return res




        