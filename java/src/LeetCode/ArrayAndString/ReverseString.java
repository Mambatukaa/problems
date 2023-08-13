package LeetCode.ArrayAndString;

import java.util.Arrays;

public class ReverseString {
    final private char[] s;

    public ReverseString(char[] s) {
        this.s = s;
    }

    public void swap(char[] s, int left, int right) {
        char temp = s[left];

        s[left] = s[right];
        s[right] = temp;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public void naive() {
        int left = 0;
        int right = s.length - 1;


        while (left < right) {
            swap(s, left, right);

            left++;
            right--;
        }

        System.out.printf(Arrays.toString(s));
    }

}
