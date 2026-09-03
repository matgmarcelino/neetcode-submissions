class Solution {
    public int[] twoSum(int[] nums, int target) {
        // first integer is complement, second integer is index of that complement
        HashMap<Integer, Integer> map = new HashMap<>();
        // target = 7
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i]; // num = 3
            int complement = target - num; // complement = 4

            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i }; // map.containsKey(4)
            }

            map.put(num, i);
        }

        return new int[] {};
    }
}
