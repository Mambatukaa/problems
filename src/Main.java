import LeetCode.ArrayAndString.StrStr;

class Main {
    public static void main(String[] args) {
        String haystack = "aaiiileeaetcode";
        String needle = "leeaet";

        StrStr strStr = new StrStr(haystack, needle);


        System.out.println(strStr.naive());


    }

}
