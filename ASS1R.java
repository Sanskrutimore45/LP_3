
public class ASS1R {

    // Method to print Fibonacci series up to 'n' terms
    public static void printFibonacciSeries(int n) {
        System.out.print("Fibonacci Series: ");
        for (int i = 0; i < n; i++) {
            System.out.print(fibonacciNumber(i) + (i < n - 1 ? ", " : ""));
        }
        System.out.println();
    }

    // Method to calculate the nth Fibonacci number
    public static int fibonacciNumber(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacciNumber(n - 1) + fibonacciNumber(n - 2);
    }

    public static void main(String[] args) {
        int n = 17; // Example number of terms
        printFibonacciSeries(n);
        System.out.println("Fibonacci(" + n + ") = " + fibonacciNumber(n));
    }
}
