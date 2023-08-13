public class Exam1 {

    static int hasSingleMaximum(int[] a) {
        if (a.length == 0) return 0;
        if (a.length == 1) return 1;

        boolean singleMax = false;
        int max = a[0];

        for (int i = 1; i < a.length; i++) {
            if (a[i] > max) {
                max = a[i];
                singleMax  = true;
            } else if (a[i] == max) {
                singleMax = false;
            }
        }

        return singleMax ? 1 : 0;
    }
}
