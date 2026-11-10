class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l: int = 0
        r: int = len(numbers) - 1

        while l < r:
            summed: int = numbers[l] + numbers[r]

            if summed > target:
                r -= 1
            elif summed < target:
                l += 1
            else:
                return [l + 1, r + 1]