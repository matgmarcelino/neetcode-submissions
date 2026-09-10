class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 1) return 1;

        Set<Character> seen = new HashSet<>();
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char curr = s.charAt(right);

            while (seen.contains(curr)) {
                seen.remove(s.charAt(left));
                left++;
            }

            seen.add(curr);
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
