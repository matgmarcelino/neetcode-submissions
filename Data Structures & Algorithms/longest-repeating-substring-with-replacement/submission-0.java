class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();
        int res = 0, l = 0, maxF = 0;

        for (int r = 0; r < s.length(); r++) {
            char currChar = s.charAt(r);
            count.put(currChar, count.getOrDefault(currChar, 0) + 1);
            maxF = Math.max(maxF, count.get(currChar));

            while ((r - l + 1) - maxF > k) {
                char leftChar = s.charAt(l);
                count.put(leftChar, count.get(leftChar) - 1);
                l++;
            }

            res = Math.max(res, r - l + 1);
        }


        return res;
    }
}
