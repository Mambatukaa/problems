package LeetCode.String;

public class StrStr {
    private final String haystack;
    private final String needle;


    public StrStr(String haystack, String needle) {
        this.haystack = haystack;
        this.needle = needle;
    }

    // Time complexity: O(n^2)
    // Space complexity: O(1)
    public int naive() {
        int needleLength = needle.length();
        // TC: O(n)
        String firstLetter = needle.substring(0, 1);

        for (int i = 0; i <= haystack.length() - needleLength; i++) {

            // TC: O(n)
            if (haystack.substring(i, i + 1).equals(firstLetter)) {
                // TC: O(n)
                String word = haystack.substring(i, i + needleLength);

                if (word.equals(needle)) {
                    return i;
                }
            }

        }


        return -1;
    }

}
