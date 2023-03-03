public class Exam2 {
    static int computeWeightedSum(int[] a) {
        int oddSum = 0;
        int evenSum = 0;

        for(int i = 0; i < a.length; i++) {
            if(a[i] % 2 == 0) {
                evenSum += a[i];
            } else {
                oddSum += a[i];
            }
        };

        return (2 * evenSum) + (3 * oddSum);
    }









}
