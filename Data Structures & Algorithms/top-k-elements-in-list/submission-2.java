class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        int n = nums.length;
        List<Integer>[] buckets = new ArrayList[n + 1];
        int[] res = new int[k];
        
        // fill map
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // fill buckets
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();

            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }

            buckets[freq].add(num);
        }
        
        // find largest k elements
        int index = 0;
        for (int i = n; i >= 0; i--) {
            if (buckets[i] == null) continue;

            for (int num : buckets[i]) {
                res[index++] = num;
                if (index == k) return res;
            }
        }
        
        return res;
    }
}
