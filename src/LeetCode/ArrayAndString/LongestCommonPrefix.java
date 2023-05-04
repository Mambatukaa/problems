package LeetCode.ArrayAndString;

public class LongestCommonPrefix {
    private final String[] strs;


    public LongestCommonPrefix(String[] strs) {
        this.strs = strs;
    }


    public String naive() {
        if (strs.length == 0) {
            return "";
        }

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);

                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }


        return prefix;
    }
}
