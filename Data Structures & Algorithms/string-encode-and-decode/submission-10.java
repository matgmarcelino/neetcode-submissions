class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for (String s : strs) {
            sb.append(s.length()).append("#").append(s);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        // 5#Hello5#World
        List<String> res = new ArrayList<>();
        int idx = 0;

        while (idx < str.length()) {
            int delimIdx = str.indexOf("#", idx) + 1; // 1
            int len = Integer.parseInt(str.substring(idx, delimIdx - 1));
            int endIdx = delimIdx + len;

            String s = str.substring(delimIdx, endIdx);
            res.add(s);

            idx = endIdx;
        }

        return res;
    }
}
