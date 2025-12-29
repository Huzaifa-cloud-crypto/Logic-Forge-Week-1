"""
Logic Forge Week 1 - Challenge 3: Balanced Performance Score
Author: [Your Name]
"""

# --- 1. Brute Force Approach (O(m+n)) ---
# Merges the two arrays and finds the middle.
# Simple logic, but doesn't meet the O(log(m+n)) constraint perfectly.
def solve_brute_force(scoresA, scoresB):
    merged = sorted(scoresA + scoresB)
    total_len = len(merged)
    
    mid = total_len // 2
    
    if total_len % 2 == 1:
        return float(merged[mid])
    else:
        return (merged[mid - 1] + merged[mid]) / 2.0

# --- 2. Optimized Approach: Binary Search on Partition (O(log(min(m,n)))) ---
# Instead of merging, we find a "partition" line that divides
# both arrays into a Left Half and a Right Half.
def solve_optimized(scoresA, scoresB):
    A, B = scoresA, scoresB
    total = len(A) + len(B)
    half = total // 2
    
    # Ensure A is the smaller array so binary search is faster
    if len(B) < len(A):
        A, B = B, A
        
    l, r = 0, len(A) - 1
    
    while True:
        # i is the pointer for A, j is the pointer for B
        i = (l + r) // 2
        # j is calculated so that Left Part size is equal to Half
        j = half - (i + 1) - 1
        
        # Determine values at the partition boundaries
        # If partition is at the edge, use infinity/-infinity
        Aleft = A[i] if i >= 0 else float("-inf")
        Aright = A[i+1] if (i + 1) < len(A) else float("inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Bright = B[j+1] if (j + 1) < len(B) else float("inf")
        
        # Check if the partition is valid
        if Aleft <= Bright and Bleft <= Aright:
            # Valid partition found!
            if total % 2 == 1:
                # Odd length: The answer is the smallest value on the Right side
                return min(Aright, Bright)
            else:
                # Even length: Average of max(Left) and min(Right)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        
        elif Aleft > Bright:
            # A's left side is too big, move partition left
            r = i - 1
        else:
            # A's left side is too small, move partition right
            l = i + 1

# --- Testing the Code ---
if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2]),
        ([1, 2], [3, 4])
    ]

    print("--- Testing Optimized Solution ---")
    for sA, sB in test_cases:
        result = solve_optimized(sA, sB)
        print(f"Team A: {sA}, Team B: {sB}")
        print(f"Median: {result}")
        print("-" * 20)