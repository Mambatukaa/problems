package LeetCode;

import java.util.Arrays;

public class MergeSortedArray {
    final private int[] nums1;
    final private int[] nums2;
    final private int m;
    final private int n;

    public MergeSortedArray(int[] nums1, int[] nums2, int m, int n) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.m = m;
        this.n = n;
    }

    public void naive() {
        int[] nums1Copy = nums1.clone();

        int p1 = 0;
        int p2 = 0;

        for (int i = 0; i < m + n; i++) {
            if (p2 >= n || (p1 < m && nums1Copy[p1] < nums2[p2])) {
                nums1[i] = nums1Copy[p1++];
            } else {
                nums1[i] = nums2[p2++];
            }

            System.out.println(Arrays.toString(nums1));
        }


    }


}
