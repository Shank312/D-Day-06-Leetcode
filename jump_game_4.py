
from collections import deque
class Solution:
  def maxResult(self, nums, k):
    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0]            # base: starting score
    dq = deque([0])            # store indices with best dp values

    for i in range(1, n):
        dp[i] = nums[i] + dp[dq[0]]   # best prev within k steps

        # maintain deque decreasing in dp values
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        dq.append(i)

        # remove out-of-window indices
        if dq[0] <= i-k:
            dq.popleft()
        
    return dp[-1]

