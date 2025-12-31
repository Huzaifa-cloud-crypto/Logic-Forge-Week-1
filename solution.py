"""
Logic Forge Week 1 - Challenge 5: Fix the Broken Expression
Author: [Your Name]
"""

# --- Initial Approach: Brute Force (BFS) ---
# Logic: Try removing 0 parentheses. If invalid, try removing 1. 
# If invalid, try removing 2... until we find valid ones.
# Time Complexity: O(2^N) - Exponential, but acceptable for N=25.

def is_valid(s):
    count = 0
    for char in s:
        if char == '(': count += 1
        elif char == ')': count -= 1
        if count < 0: return False
    return count == 0

def solve_brute_force(s):
    # 'level' stores all strings with the current number of removals
    level = {s} 
    
    while True:
        valid_strings = []
        for elem in level:
            if is_valid(elem):
                valid_strings.append(elem)
        
        # If we found valid strings at this level, return them!
        # Because BFS finds the shortest path, these are guaranteed to be minimum removals.
        if valid_strings:
            return sorted(valid_strings)
        
        # If not, generate the next level (remove 1 more char)
        next_level = set()
        for elem in level:
            for i in range(len(elem)):
                # Only remove parentheses, not letters
                if elem[i] in "()":
                    new_s = elem[:i] + elem[i+1:]
                    next_level.add(new_s)
        
        level = next_level
        # Safety break for empty levels
        if not level:
            return [""]

# --- Testing ---
if __name__ == "__main__":
    test_cases = ["()())()", "(a)())()", ")(", "((("]
    for expr in test_cases:
        print(f"Input: {expr} -> Output: {solve_brute_force(expr)}")