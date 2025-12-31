"""
Logic Forge Week 1 - Challenge 4: The Deep Storage Inventory Search
Author: [Your Name]
"""

# --- Initial Approach: Brute Force (Flatten & Sort) ---
# Logic: Treat the 2D matrix as one big bag of numbers.
# Pull them all out, sort them, and pick the k-th one.
# Time Complexity: O(N^2 log(N^2)) - Very slow for large warehouses.
# Space Complexity: O(N^2) - Uses a lot of extra memory.

def kth_smallest(matrix, k):
    # 1. Flatten the 2D matrix into a single list
    all_elements = []
    for row in matrix:
        for num in row:
            all_elements.append(num)
    
    # 2. Sort the entire list
    all_elements.sort()
    
    # 3. Return the k-th smallest (index is k-1)
    return all_elements[k-1]

# --- Testing ---
if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(f"Brute Force Result: {kth_smallest(matrix, k)}")