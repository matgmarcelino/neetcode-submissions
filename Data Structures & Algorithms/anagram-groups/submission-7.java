class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedS = new String(charArray);

            map.putIfAbsent(sortedS, new ArrayList<>());
            map.get(sortedS).add(s);
        }

        for (List<String> list : map.values()) {
            res.add(list);
        }

        return res;
    }
}
