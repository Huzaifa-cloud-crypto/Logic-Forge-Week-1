"""
Logic Forge Week 1 - Challenge 5: Fix the Broken Expression
Author: [Your Name]
"""
def solve_optimized(s):
    left_rem = 0
    right_rem = 0
    for char in s:
        if char == '(': left_rem += 1
        elif char == ')':
            if left_rem > 0: left_rem -= 1
            else: right_rem += 1

    result = set()
    def dfs(index, left_count, right_count, left_rem, right_rem, current_expr):
        if index == len(s):
            if left_rem == 0 and right_rem == 0 and left_count == right_count:
                result.add("".join(current_expr))
            return

        char = s[index]
        # Option A: Remove char
        if (char == '(' and left_rem > 0) or (char == ')' and right_rem > 0):
            if char == '(': dfs(index + 1, left_count, right_count, left_rem - 1, right_rem, current_expr)
            elif char == ')': dfs(index + 1, left_count, right_count, left_rem, right_rem - 1, current_expr)
        
        # Option B: Keep char
        current_expr.append(char)
        if char != '(' and char != ')': dfs(index + 1, left_count, right_count, left_rem, right_rem, current_expr)
        elif char == '(': dfs(index + 1, left_count + 1, right_count, left_rem, right_rem, current_expr)
        elif char == ')' and right_count < left_count: dfs(index + 1, left_count, right_count + 1, left_rem, right_rem, current_expr)
        current_expr.pop()

    dfs(0, 0, 0, left_rem, right_rem, [])
    return list(result)

if __name__ == "__main__":
    print(solve_optimized("()())()"))