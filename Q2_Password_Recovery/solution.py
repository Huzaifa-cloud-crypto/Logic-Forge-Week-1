"""
Logic Forge Week 1 - Challenge 2: Password Recovery Window
Author: [Your Name]
"""
from collections import Counter

# --- 1. Brute Force Approach (O(n^3)) ---
# Checks every single substring to see if it contains the pattern.
# WARNING: extremely slow for large inputs!
def solve_brute_force(log, pattern):
    n = len(log)
    min_len = float('inf')
    result = ""
    
    # Check every possible start and end point
    for i in range(n):
        for j in range(i, n):
            sub = log[i : j+1]
            
            # Check if this substring has all needed characters
            # We use Counters to compare frequencies
            sub_count = Counter(sub)
            pattern_count = Counter(pattern)
            
            is_valid = True
            for char, count in pattern_count.items():
                if sub_count[char] < count:
                    is_valid = False
                    break
            
            if is_valid:
                if len(sub) < min_len:
                    min_len = len(sub)
                    result = sub
                    
    return result

# --- 2. Optimized Approach: Sliding Window (O(n)) ---
# Uses the "Elastic Band" strategy.
def solve_optimized(log, pattern):
    if not pattern or not log:
        return ""

    # Frequency map for the required pattern
    dict_t = Counter(pattern)
    required = len(dict_t)  # Number of unique characters we need to satisfy

    # Window pointers
    l, r = 0, 0
    
    # formed is how many unique characters in current window match the required frequency in pattern
    formed = 0
    
    # Dictionary to keep track of all the unique characters in the current window
    window_counts = {}

    # ans tuple of form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(log):
        # Add one character from the right to the window
        character = log[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in pattern
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'
        while l <= r and formed == required:
            character = log[l]

            # Save the smallest window until now
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window
            l += 1    

        # Keep expanding the window once we are done contractiing
        r += 1    

    return "" if ans[0] == float("inf") else log[ans[1] : ans[2] + 1]

# --- Testing the Code ---
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa")
    ]

    print("--- Testing Optimized Solution ---")
    for log, pattern in test_cases:
        result = solve_optimized(log, pattern)
        print(f"Log: {log}, Pattern: {pattern}")
        print(f"Output: '{result}'")
        print("-" * 20)