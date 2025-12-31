"""
Logic Forge Week 1 - Challenge 4: The Deep Storage Inventory Search
Author: [Your Name]
"""

# --- Optimized Approach: Binary Search on Value Range ---
# Logic: Instead of sorting indices, we guess a value 'mid' 
# and count how many numbers in the matrix are <= mid.
# Time Complexity: O(N * log(Max-Min)) - Much faster and uses O(1) memory.

def count_less_equal(matrix, mid):
    """ Helper: Counts how many numbers in matrix are <= mid """
    count = 0
    n = len(matrix)
    # Start from bottom-left corner
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] <= mid:
            # If current is <= mid, then everything above it is also <= mid
            count += (row + 1)
            col += 1
        else:
            row -= 1
    return count

def kth_smallest(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[n-1][n-1]
    
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(matrix, mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

# --- Testing ---
if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(f"Optimized Result: {kth_smallest(matrix, k)}")