class Solution:

    def encode(self, strs: List[str]) -> str:    
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        idx: int = 0

        while (idx < len(s)):
            delim_idx: int = s.find("#", idx);
            str_len: int = int(s[idx:delim_idx])
            idx = delim_idx + 1 + str_len
            res.append(s[delim_idx + 1 : delim_idx + 1 + str_len])

        return res