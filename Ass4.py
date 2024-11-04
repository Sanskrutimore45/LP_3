def knapsack(weights, values, capacity):
    n = len(weights)

    # Create a table to store the maximum value for each capacity and item count
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If the current item can fit in the knapsack
            if weights[i - 1] <= w:
                # Choose the maximum of including or excluding the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the item cannot fit, just carry forward the previous value
                dp[i][w] = dp[i - 1][w]

    # The maximum value will be found in dp[n][capacity]
    max_value = dp[n][capacity]

    # To find which items are included, backtrack through the table
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    # Reverse the selected_items list to get the correct order
    selected_items.reverse()

    return max_value, selected_items

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value, selected_items = knapsack(weights, values, capacity)

print(f"Maximum value: {max_value}")
print(f"Selected items: {selected_items}")
