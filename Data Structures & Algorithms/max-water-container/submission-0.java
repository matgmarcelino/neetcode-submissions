class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int max = 0;

        while (left < right) {
            int volume = (right - left) * Math.min(heights[left], heights[right]);
            max = Math.max(max, volume);

            if (heights[left] > heights[right]) {
                right--;
                continue;
            }

            left++;
        }

        return max;
    }
}
