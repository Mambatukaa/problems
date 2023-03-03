public class Exam3 {
    static boolean isPrime(int num) {
        for (int j = 2; j < num; j++) {
            if (num % j == 0) {
                return false;
            }
        }

        return true;
    }


    static int isPrimeHappy(int n) {
        if (n < 3) return 0;

        int primeSum = 0;

        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primeSum += i;
            }
        }

        return primeSum % n == 0 ? 1 : 0;
    }


}
