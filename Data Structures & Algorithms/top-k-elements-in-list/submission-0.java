class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        // build frequency map
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // create bucket array; index is frequency, value is num
        List<Integer>[] buckets = new List[nums.length + 1];

        // populate buckets with matching frequency
        for (int key : freqMap.keySet()) {
            int frequency = freqMap.get(key);

            if (buckets[frequency] == null)
                buckets[frequency] = new ArrayList<>();
            
            buckets[frequency].add(key);
        }

        // find top k elements

        int[] result = new int[k];
        int index = 0;

        for (int i = buckets.length - 1; i >= 0 && index < k; i--) {
            if (buckets[i] == null) {
                continue;
            }

            for (int num : buckets[i]) {
                result[index++] = num;
                if (index == k) return result;
            }
        }

        return result;
    }
}
