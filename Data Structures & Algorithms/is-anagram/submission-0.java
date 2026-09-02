class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> mapS = new HashMap();
        HashMap<Character, Integer> mapT = new HashMap();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (mapS.containsKey(c)) {
                mapS.put(c, mapS.get(c) + 1);
                continue;
            }

            mapS.put(c, 1);
        }

        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);

            if (mapT.containsKey(c)) {
                mapT.put(c, mapT.get(c) + 1);
                continue;
            }

            mapT.put(c, 1);
        }

        return mapS.entrySet().equals(mapT.entrySet());
    }
}
