class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);

            if (!Character.isLetterOrDigit(leftChar)) {
                left++;
                continue;
            }

            if (!Character.isLetterOrDigit(rightChar)) {
                right--;
                continue;
            }

            leftChar = Character.toLowerCase(leftChar);
            rightChar = Character.toLowerCase(rightChar);

            if (leftChar != rightChar) return false;

            left++;
            right--;
        }

        return true;
    }
}
