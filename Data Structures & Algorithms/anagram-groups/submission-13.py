class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: List[List[str]] = []
        seen: dict[str, List[str]] = defaultdict(list)

        for s in strs:
            sortedS: str = "".join(sorted(s))
            seen[sortedS].append(s)

        for val in seen.values():
            res.append(val)

        return res





        