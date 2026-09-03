class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List> map = new HashMap<>();

        for (String s : strs) {
            // sort String
            char[] temp = s.toCharArray();
            Arrays.sort(temp);
            String sorted = String.valueOf(temp);

            // if map has key, append current string
            if (map.containsKey(sorted)) {
                map.get(sorted).add(s);
                continue;
            }

            // otherwise create list and append current string
            List<String> list = new ArrayList<>();
            list.add(s);
            map.put(sorted, list);
        }

        // iterate through map and add to List<List<String>>
        List<List<String>> result = new ArrayList<>();

        for (String key : map.keySet()) {
            result.add(map.get(key));
        }

        return result;

    }
}
