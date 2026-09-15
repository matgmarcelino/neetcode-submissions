class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int left = 0, longest = 0;

        for (int right = 0; right < s.length(); right++) {
            char currChar = s.charAt(right);

            while (set.contains(currChar)) {
                set.remove(s.charAt(left));
                left++;
            }

            set.add(currChar);
            longest = Math.max(longest, right - left + 1);
        }

        return longest;
    }
}
