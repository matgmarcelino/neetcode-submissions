class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, List[str]] = defaultdict(list)
        
        for s in strs:
            sorted_s: str = "".join(sorted(s))
            groups[sorted_s].append(s)

        return list(groups.values())