
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], H: int) -> int:
        lo, hi = 1, max(piles)    
        step = 1                  
        
        while lo<hi:
            mid = (lo + hi)//2   

            hours = sum((p + mid - 1) // mid for p in piles)
            if hours <= H:
                hi = mid 
            else:
                lo = mid + 1
        return lo



        
        
       