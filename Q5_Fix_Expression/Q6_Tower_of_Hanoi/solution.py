"""
Logic Forge Week 1 - Challenge 6: Tower of Hanoi Algorithm
Author: [Your Name]
"""

# --- Recursive Approach ---
# Logic: Move N-1 disks to the auxiliary rod, move the largest disk to the target,
# then move the N-1 disks from auxiliary to target.
# Time Complexity: O(2^n) - The number of moves doubles with each disk.

def tower_of_hanoi(n, source, destination, auxiliary):
    # Base Case: If only 1 disk, just move it directly.
    if n == 1:
        print(f"Disk 1 moved from {source} to {destination}")
        return
    
    # Step 1: Move top n-1 disks from Source -> Auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Step 2: Move the nth (largest) disk from Source -> Destination
    print(f"Disk {n} moved from {source} to {destination}")
    
    # Step 3: Move the n-1 disks from Auxiliary -> Destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# --- Testing ---
if __name__ == "__main__":
    n = 3
    print(f"--- Tower of Hanoi Solution for N={n} ---")
    # A is Source, C is Destination, B is Auxiliary
    tower_of_hanoi(n, 'A', 'C', 'B')