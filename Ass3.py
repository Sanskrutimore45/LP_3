class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    # Sort items by profit-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    final_value = 0.0  # Variable to store the final maximum profit

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            final_value += item.profit
        else:
            final_value += item.profit * (W / item.weight)
            break

    return final_value

if __name__ == "__main__":
    W = 50
    arr = [Item(120, 30), Item(100, 20), Item(60, 10)]

    max_val = fractionalKnapsack(W, arr)
    print("Maximum value in Knapsack =", max_val)
