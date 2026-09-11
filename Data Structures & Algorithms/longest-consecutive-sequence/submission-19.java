class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int maxLen = 0;
        for (int num : nums) {
            if (set.contains(num - 1)) continue;

            int length = 1;
            while (set.contains(num + length)) {
                length++;
            }

            maxLen = Math.max(length, maxLen);
        }

        return maxLen;
    }
}
