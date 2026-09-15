class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] buckets = new ArrayList[nums.length + 1];
        // index = freq | val = num

        for (int num : freqMap.keySet()) {
            int freq = freqMap.get(num);

            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }

            buckets[freq].add(num);
        }

        int[] res = new int[k];
        int idx = 0;

        for (int i = buckets.length - 1; i >= 0; i--) {
            if (buckets[i] == null) continue;

            for (int num : buckets[i]) {
                res[idx++] = num;

                if (idx == k) {
                    return res;
                }
            }
        }

        return res;
    }
}
