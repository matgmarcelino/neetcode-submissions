class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length()).append("#").append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {

            // find index of next delimiter
            int delimiterIdx = str.indexOf("#", i);

            // extract length of next word
            int length = Integer.parseInt(str.substring(i, delimiterIdx));

            // move past delimiter
            i = delimiterIdx + 1;

            // extract string based of length
            String s = str.substring(i, i + length);
            result.add(s);

            i += length;
        }

        return result;
    }
}
