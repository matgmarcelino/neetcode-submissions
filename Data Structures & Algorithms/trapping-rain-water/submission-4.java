class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int maxLeft[] = new int[n];
        int maxRight[] = new int[n];
        int min[] = new int[n];

        int max = 0;
        for (int i = 1; i < n; i++) {
            max = Math.max(max, height[i - 1]);
            maxLeft[i] = max;
        }

        max = 0;
        for (int i = n - 2; i >= 0; i--) {
            max = Math.max(max, height[i + 1]);
            maxRight[i] = max;
        }

        for (int i = 0; i < n; i++) {
            min[i] = Math.min(maxLeft[i], maxRight[i]);
        }

        int total = 0;
        for (int i = 0; i < n; i++) {
            int vol = min[i] - height[i];
            total += Math.max(vol, 0);
        }
        return total;
    }
}
