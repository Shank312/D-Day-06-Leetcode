
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return []
        
        dq = deque() # Deque will store indices of elements in 'nums'
                     # and maintain decreasing order of values 
        res = []            # To store the maximum of each window

        for i, x in enumerate(nums):
            # 1. Remove indices from the front if they are out of the current window 
            # Window range: [i - k + 1, i]
            while dq and dq[0] <= i - k:
                dq.popleft()
            # 2. Maintain decreasing order in deque
            while dq and nums[dq[-1]] < x:
                dq.pop()
            # 3. Add the current index into the deque 
            dq.append(i)

            # 4. Once we've processed at least 'k' elements, record the maximum
            # The maximum is always at the front of the deque
            if i>=k-1:
                res.append(nums[dq[0]])
        return res
        