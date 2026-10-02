class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complMap = {}

        for i, val in enumerate(nums):
            compl = target - val

            if compl in complMap:
                return [complMap[compl], i]
            
            complMap[val] = i
        
        return [-1, -1]