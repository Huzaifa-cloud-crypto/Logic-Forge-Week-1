"""
Logic Forge Week 1 - Challenge 1: Team Contribution Multiplier
Author: [M.Huzaifa]
"""

# --- 1. Brute Force Approach (O(n^2)) ---

def solve_brute_force(contributions):
    n = len(contributions)
    impact = []
    
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:  # Multiply everyone EXCEPT the current person
                product *= contributions[j]
        impact.append(product)
        
    return impact
# --- Testing the Code ---
print(solve_brute_force([1, 2, 3, 4]))  # Expected Output: [24, 12, 8, 6]
print(solve_brute_force([-1, 1, 0, -3, 3]))
# --- 2. Optimized Approach (O(n)) ---
# Uses the "Left and Right Pass" strategy.
def solve_optimized(contributions):
    n = len(contributions)
    if n == 0:
        return []
    
    impact = [1] * n  # Initialize result array with 1s

    # Pass 1: Calculate Left Products
    # For each index i, 'left_product' is the product of everything to the left of i.
    left_product = 1
    for i in range(n):
        impact[i] = left_product
        left_product *= contributions[i]
    
    # Pass 2: Calculate Right Products & Final Result
    # For each index i, 'right_product' is the product of everything to the right of i.
    # We multiply this into our existing 'impact' array.
    right_product = 1
    for i in range(n - 1, -1, -1):  # Loop backwards from end to start
        impact[i] *= right_product
        right_product *= contributions[i]
        
    return impact

# --- Testing the Code ---
print(solve_optimized([1, 2, 3, 4]))  # Expected Output: [24, 12, 8, 6]
print(solve_optimized([-1, 1, 0, -3, 3]))  # Expected Output: [0, 0, 9, 0, 0]