def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0.0  # Track the total value of items in the knapsack
    knapsack_contents = []  # To store items (or fractions) added to knapsack

    for item_id, value, weight in items:
        if capacity == 0:  # Knapsack is full
            break

        if weight <= capacity:
            # If the whole item can be added
            capacity -= weight
            total_value += value
            knapsack_contents.append((item_id, 1))  # 1 means full item added
        else:
            # If only part of the item can be added
            fraction = round(capacity / weight , 2)
            total_value += value * fraction
            knapsack_contents.append((item_id, fraction))
            capacity = 0  # Knapsack is now full

    return total_value, knapsack_contents

# Example usage
items = [
    ('item1', 60, 10),  # (item_id, value, weight)
    ('item2', 100, 20),
    ('item3', 120, 30)
]
capacity = 50
total_value, knapsack_contents = fractional_knapsack(items, capacity)
print("Maximum value in knapsack:", total_value)
print("Items in knapsack (item_id, fraction):", knapsack_contents)
