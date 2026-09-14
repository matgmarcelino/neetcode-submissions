class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int left = 0, right = n - 1;
        int max = 0;

        while (left < right) {
            int heightLeft = heights[left];
            int heightRight = heights[right];
            int vol = Math.min(heightLeft, heightRight) * (right - left);
            max = Math.max(vol, max);

            if (heightLeft > heightRight) {
                right--;
                continue;
            }

            left++;
        }

        return max;
    }
}
