class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for (String s : strs) {
            sb.append(s.length()).append("#").append(s);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int index = 0;
        while (index < str.length()) {
            int delimiterIdx = str.indexOf("#", index); 
            String s = str.substring(index, delimiterIdx);
            int len = Integer.parseInt(s);
            int endIndex = index + s.length() + len + 1;
            String word = str.substring(delimiterIdx + 1, endIndex);
            System.out.println(word);
            
            res.add(word);
            index = endIndex;
        }

        return res;
    }
}
