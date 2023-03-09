import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums1 = {1, 2, 0};
        int[] nums2 = {1};
        int m = 2;
        int n = 1;

        MergeSortedArray mergeSortedArray = new MergeSortedArray(nums1, nums2, m, n);

        mergeSortedArray.naive();


    }

}
