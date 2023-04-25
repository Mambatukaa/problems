package LeetCode.ArrayAndString;

public class LongestCommonPrefix {
    private final String[] strs;


    public LongestCommonPrefix(String[] strs) {
        this.strs = strs;
    }


    public String naive() {
        StringBuilder ans = new StringBuilder();
        int i = 0;
        String firstEl = strs[0];

        while (i <= firstEl.length()) {
            char curr = firstEl.charAt(i);

            for (int j = 0; j < strs.length; j++) {
                if (ans.length() > strs[j].length() - 1 || curr != strs[j].charAt(i)) {
                    return ans.toString();
                }
            }

            ans.append(curr);
            i++;
        }

        return ans.toString();
    }
}
