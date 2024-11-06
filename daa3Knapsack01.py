def knapsack_01(items, capacity):
    # Number of items
    n = len(items)
    
    # Initialize a 2D DP array with zeros (dimensions: (n+1) x (capacity+1))
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        item_id, value, weight = items[i - 1]  # Get current item's value and weight
        for w in range(capacity + 1):
            if weight <= w:
                # Take the maximum of including or excluding the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                # Cannot include the current item
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items that make up the maximum value
    w = capacity
    knapsack_contents = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # If the item was included
            item_id, value, weight = items[i - 1]
            knapsack_contents.append(item_id)
            w -= weight  # Reduce weight capacity

    max_value = dp[n][capacity]
    return max_value, knapsack_contents[::-1]  # Return items in original order

items = [
    ('item1', 10, 10),  # (item_id, value, weight)
    ('item2', 20, 20),
    ('item3', 30, 30),
    ('item4', 40, 40),
    ('item5', 50, 80),
    ('item6', 60, 80)
]
capacity = 200
max_value, knapsack_contents = knapsack_01(items, capacity)
print("Maximum value in knapsack:", max_value)
print("Items in knapsack:", knapsack_contents)
