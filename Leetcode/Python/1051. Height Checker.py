from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Sort the heights to get the expected order
        expected = sorted(heights)
        mismatch_count = 0
        
        # Compare each element of the original list with the sorted list
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
        
        # Return the number of mismatches
        return mismatch_count
