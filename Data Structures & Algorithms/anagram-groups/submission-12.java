class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] sArray = s.toCharArray();
            Arrays.sort(sArray);
            String sortedS = new String(sArray);

            map.putIfAbsent(sortedS, new ArrayList<>());

            map.get(sortedS).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
