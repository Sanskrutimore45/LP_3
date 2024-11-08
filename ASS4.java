
public class ASS4 {

    // Returns the maximum value that can be put in a knapsack of capacity W
    public static int knapsack(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        // Create a 2D array to store the maximum value at each n and capacity
        int[][] dp = new int[n + 1][capacity + 1];
        // Build the dp array in a bottom-up manner
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (i == 0 || w == 0) {
                    dp[i][w] = 0; // Base case: no items or zero capacity
                } else if (weights[i - 1] <= w) {
                    dp[i][w] = Math.max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        return dp[n][capacity];
    }

    public static void main(String[] args) {
        int[] values = {60, 100, 120};
        int[] weights = {10, 20, 30};
        int capacity = 50;

        int maxValue = knapsack(weights, values, capacity);
        System.out.println("Maximum value in Knapsack = " + maxValue);
    }
}
