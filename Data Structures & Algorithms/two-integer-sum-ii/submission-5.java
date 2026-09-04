class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int first = 0;
        int second = numbers.length - 1;

        while (first < second) {
            int sum = numbers[first] + numbers[second];
            if (sum < target)  {
                first++;
                continue;
            }

            if (sum > target) {
                second--;
                continue;
            }

            return new int[] { first + 1, second + 1 };
        }

        return new int[2];
    }
}
