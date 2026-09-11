class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int maxLen = 0;
        for (int num : nums) {
            if (set.contains(num - 1)) continue;

            int count = 1;
            while (set.contains(num + 1)) {
                num++;
                count++;
            }

            maxLen = Math.max(count, maxLen);
        }

        return maxLen;
    }
}
