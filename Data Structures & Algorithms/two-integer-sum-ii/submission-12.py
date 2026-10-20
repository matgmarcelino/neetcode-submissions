class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l: int = 0
        r: int = len(numbers) - 1

        while (l <= r):
            added: int = numbers[l] + numbers[r]

            if added > target:
                r -= 1
                continue

            if added < target:
                l += 1
                continue

            return [l + 1, r + 1]

        return [-1, -1]


