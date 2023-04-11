import LeetCode.*;
import LeetCode.String.StrStr;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        String haystack = "aaiiileeaetcode";
        String needle = "leeaet";

        StrStr strStr = new StrStr(haystack, needle);


        System.out.println(strStr.naive());


    }

}
