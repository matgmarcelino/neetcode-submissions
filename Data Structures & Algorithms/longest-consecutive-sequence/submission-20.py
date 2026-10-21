class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen: Set[int] = set(nums)
        longest: int = 0

        for num in nums:
            if num - 1 in seen:
                continue
            
            length: int = 1
            current: int = num + 1
            while num + length in seen:
                length += 1
                
            longest = max(longest, length)

        return longest
                