class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        

        while (start <= end) {
            char startChar = Character.toLowerCase(s.charAt(start));
            char endChar = Character.toLowerCase(s.charAt(end));

            if (!Character.isLetterOrDigit(startChar)) {
                start++;
                continue;
            }

            if (!Character.isLetterOrDigit(endChar)) {
                end--;
                continue;
            }

            if (startChar != endChar) return false;

            start++;
            end--;
        }

        return true;
    }
}
