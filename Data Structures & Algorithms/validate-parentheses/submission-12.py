class Solution:
    def isValid(self, s: str) -> bool:
        openTo: dict[str, str] = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        stack: list[str] = []

        for c in s:
            if c in openTo:
                if stack and stack.pop() == openTo[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
