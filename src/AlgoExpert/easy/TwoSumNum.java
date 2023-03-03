package AlgoExpert.easy;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class TwoSumNum {
    private final int[] arr;
    private final int targetSum;

    public TwoSumNum(int[] arr, int targetSum) {
        this.arr = arr;
        this.targetSum = targetSum;
    }

    /* if any two numbers in the input array sum up to the target sum,
     the target sum, the function should return them in array */

    /* if no two numbers sum up to the target sum, the function should
    return an empty array
    */

    // Space: O(n) | Time: O(n)
    public int[] hashSetSolution() {
        Set<Integer> visitedSet = new HashSet<Integer>(); // Space: O(n)

        int counter = 1;

        for (int num : arr) {
            System.out.println(counter);

            if (visitedSet.contains(targetSum - num)) {
                return new int[]{targetSum - num, num};
            } else {
                visitedSet.add(num);
            }

            counter++;
        }

        return new int[]{};
    }


    // Space: O(1) | Time: O(nLog(n))
    public int[] sortedSolution() {
        // sorted... {1,2,3,4,5,6}, 10
        int left = 0;
        int right = arr.length - 1;


        while (left < right) {
            if (arr[left] + arr[right] == targetSum) {
                return new int[]{arr[right], arr[left]};
            }

            if (arr[left] + arr[right] < targetSum) {
                left++;
            } else {
                right--;
            }
        }


        return new int[]{};
    }


    // Space: O(1) | Time: O(n^2)

    public int[] nestedLoopSolution() {
        for (int i = 0; i < arr.length; i++) {
            for (int j = i; j < arr.length; j++) {
                if (arr[i] + arr[j] == targetSum) {
                    return new int[]{arr[j], arr[i]};
                }
            }
        }

        return new int[]{};
    }

    public static int log(int target) {
        System.out.println(target + 2);

        return target;
    }

}
