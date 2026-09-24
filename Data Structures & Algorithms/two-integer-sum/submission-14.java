class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Num : Index
        Map<Integer, Integer> complementMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int compl = target - num;

            if (complementMap.containsKey(compl)) {
                return new int[] { complementMap.get(compl), i  };
            }

            complementMap.put(num, i);
        }

        return new int[2];
    }
}
