class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        List<List<String>> res = new ArrayList<>();

        for (String s : strs) {
            char[] sArray = s.toCharArray();
            Arrays.sort(sArray);
            String sortedS = new String(sArray);

            map.putIfAbsent(sortedS, new ArrayList<>());

            map.get(sortedS).add(s);
        }

        for (List<String> list : map.values()) {
            res.add(list);
        }

        return res;
    }
}
