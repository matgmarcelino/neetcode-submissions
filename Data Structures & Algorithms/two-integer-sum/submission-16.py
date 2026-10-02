class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            compl = target - val

            if compl in seen:
                return [seen[compl], i]
            
            seen[val] = i