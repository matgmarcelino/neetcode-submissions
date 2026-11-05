class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: map[int, int] = {}

        for i, num in enumerate(nums):
            complement: int = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        