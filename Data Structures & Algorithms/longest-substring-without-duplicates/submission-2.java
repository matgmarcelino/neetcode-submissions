class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 1) return 1;

        Set<Character> seen = new HashSet<>();
        int maxLength = 0, left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currChar = s.charAt(right);

            while (seen.contains(currChar)) {
                seen.remove(s.charAt(left));
                left++;
            }

            seen.add(currChar);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
