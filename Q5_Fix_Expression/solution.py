"""
Logic Forge Week 1 - Challenge 5: Fix the Broken Expression
Author: [Your Name]
"""
def is_valid(s):
    count = 0
    for char in s:
        if char == '(': count += 1
        elif char == ')': count -= 1
        if count < 0: return False
    return count == 0

def solve_brute_force(s):
    level = {s} 
    while True:
        valid_strings = []
        for elem in level:
            if is_valid(elem):
                valid_strings.append(elem)
        if valid_strings:
            return sorted(valid_strings)
        next_level = set()
        for elem in level:
            for i in range(len(elem)):
                if elem[i] in "()":
                    new_s = elem[:i] + elem[i+1:]
                    next_level.add(new_s)
        level = next_level
        if not level: return [""]

if __name__ == "__main__":
    print(solve_brute_force("()())()"))