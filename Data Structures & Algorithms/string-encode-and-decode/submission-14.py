class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while (index < len(s)):
            delim_idx = s.find('#', index)
            str_len = int(s[index:delim_idx])

            start_idx = delim_idx + 1
            end_idx = str_len + start_idx
            res.append(s[start_idx:end_idx])
            index = end_idx

        return res

