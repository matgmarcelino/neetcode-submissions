class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // index = frequency | val = num
        List<Integer>[] buckets = new List[nums.length + 1];

        for (int num : freqMap.keySet()) {
            int freq = freqMap.get(num);
            
            if (buckets[freq] == null) buckets[freq] = new ArrayList<>();

            buckets[freq].add(num);
        }

        int[] res = new int[k];
        int index = 0;

        for (int i = buckets.length - 1; i >= 0 && index < k; i--) {
            if (buckets[i] == null) continue;
            for (int num : buckets[i]) {
                res[index++] = num;
                if (index == k) return res;
            }
        }

        return res;
    }
}
