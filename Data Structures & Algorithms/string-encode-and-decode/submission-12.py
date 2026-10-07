class Solution:

    def encode(self, strs: List[str]) -> str:
       return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        idx: int = 0

        while idx < len(s):
            delim_idx: int = s.index("#", idx)
            substring_len: int = int(s[idx : delim_idx])

            str_start: int = delim_idx + 1
            str_end: int = delim_idx + 1 + substring_len

            res.append(s[str_start:str_end])

            idx = str_end

        return res


        
