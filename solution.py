"""
Logic Forge Week 1 - Challenge 5: Fix the Broken Expression
Author: [Your Name]
"""

# --- Optimized Approach: DFS with Pruning ---
# Logic: 
# 1. First, count exactly how many left '(' and right ')' parentheses 
#    must be removed to make it valid.
# 2. Use Recursion (DFS) to remove exactly that many characters.
# Time Complexity: O(2^N) worst case, but heavily pruned, so much faster in practice.

def solve_optimized(s):
    # Step 1: Count misplaced parentheses
    left_rem = 0
    right_rem = 0
    for char in s:
        if char == '(':
            left_rem += 1
        elif char == ')':
            if left_rem > 0:
                left_rem -= 1  # This ')' matches a previous '('
            else:
                right_rem += 1 # This ')' is extra

    result = set()

    # Step 2: DFS function
    def dfs(index, left_count, right_count, left_rem, right_rem, current_expr):
        # Base Case: We reached the end of the string
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                if left_count == right_count:
                    result.add("".join(current_expr))
            return

        char = s[index]

        # Option A: Remove the character (only if allowed)
        if (char == '(' and left_rem > 0) or (char == ')' and right_rem > 0):
            # Try skipping this char
            if char == '(':
                dfs(index + 1, left_count, right_count, left_rem - 1, right_rem, current_expr)
            elif char == ')':
                dfs(index + 1, left_count, right_count, left_rem, right_rem - 1, current_expr)

        # Option B: Keep the character
        current_expr.append(char)
        if char != '(' and char != ')':
            # It's a letter, just keep going
            dfs(index + 1, left_count, right_count, left_rem, right_rem, current_expr)
        elif char == '(':
            # Keep '(', increment count
            dfs(index + 1, left_count + 1, right_count, left_rem, right_rem, current_expr)
        elif char == ')' and right_count < left_count:
            # Keep ')', ONLY if it matches an open '(' (Pruning invalid states early)
            dfs(index + 1, left_count, right_count + 1, left_rem, right_rem, current_expr)
        
        # Backtrack: remove the char we just added to try other paths
        current_expr.pop()

    # Start the search
    dfs(0, 0, 0, left_rem, right_rem, [])
    return list(result)

# --- Testing ---
if __name__ == "__main__":
    test_cases = ["()())()", "(a)())()", ")(", "((("]
    print("--- Testing Optimized DFS Solution ---")
    for expr in test_cases:
        print(f"Input: {expr} -> Output: {solve_optimized(expr)}")