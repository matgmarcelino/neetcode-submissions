class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, List[str]] = defaultdict(list)
        for s in strs:
            sorted_s: str = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        
        return list(anagrams.values())