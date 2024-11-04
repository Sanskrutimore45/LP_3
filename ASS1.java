
public class ASS1 {

    public static void printFibonacciSeries(int n) {
        if (n <= 0) {
            System.out.println("Enter positive number ");
            return;
        }
        int a = 0, b = 1;
        System.out.print("Fibonacci Series = " + a + ",");
        for (int i = 1; i < n; i++) {
            System.out.print(b + ",");
            int next = a + b;
            a = b;
            b = next;
        }
        System.out.println();
    }

    public static int fibonacciNumber(int n) {
        if (n <= 1) {
            return n;
        }

        int a = 0, b = 1, result = 0;

        for (int i = 2; i <= n; i++) {
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 17;
        printFibonacciSeries(n);
        System.out.println("Fibonacci(" + n + ") = " + fibonacciNumber(n));
    }
}
