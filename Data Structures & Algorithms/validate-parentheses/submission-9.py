class Solution:
    def isValid(self, s: str) -> bool:
        openTo: dict[str, str] = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack: List[str] = []
        for ch in s:
            if ch in openTo:
                if stack and stack.pop() == openTo[ch]:
                    continue
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0

