class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded: List[str] = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        idx: int = 0
        while idx < len(s):
            delim_idx: int = s.find("#", idx)
            str_len: int = int(s[idx:delim_idx])

            start: int = delim_idx + 1
            end: int = start + str_len
            res.append(s[start:end])

            idx = end

        return res