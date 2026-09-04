class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int maxLength = 0;

        for (int num : nums) {
            set.add(num);
        }

        
        for (int num : set) {
            if (set.contains(num - 1)) continue;

            int length = 1;
            int currNum = num + 1;
            while (set.contains(currNum)) {
                length++;
                currNum++;
            }

            if (length > maxLength) maxLength = length;
        }

        return maxLength;
    }
}
